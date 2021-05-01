from django.shortcuts import render,redirect,get_object_or_404
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Contacts,Call,Text,TextSave,Emailing
from django.contrib.auth.models import User
from django.views.generic import ListView,CreateView,UpdateView,DeleteView,DetailView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_exempt
import os
from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse
from Smartphone_sim.settings import TWILIO_AUTH_SID, TWILIO_AUTH_TOKEN
from django.conf import settings
from django import forms
import twilio
import smtplib, ssl
from collections import Counter
# Create your views here.

@login_required
def communcation_view(request):
    return render(request,"Communication/communication.html",{})

@login_required
def call_view(request):
    return render(request,"Communication/Call_View.html",{})

@login_required
def make_a_call_view(request):
    return render(request,"Communication/make_call.html",{})

@login_required
def calling(request):
    if request.POST:
        global number
        number = request.POST['number']
        try:
            account_sid = TWILIO_AUTH_SID
            auth_token = TWILIO_AUTH_TOKEN
            client = Client(account_sid, auth_token)

            call = client.calls.create(
                                    url='http://demo.twilio.com/docs/voice.xml',
                                    to=number,
                                    from_='+19564136773')

            print(call.sid)
        except twilio.base.exceptions.TwilioRestException as e:
            return render(request, "Communication/bad_number.html")
        try:
            numbers = Contacts.objects.all().filter(Whos_Phone=request.user.username, mobile_number = number).get()
            print(numbers.contact_name)
            if numbers!= None:
                who = numbers.contact_name
            else:
                who = number
        except Contacts.DoesNotExist as e:
            who = number
        Call.objects.create(
        caller1 = request.user,
        caller = request.user.username,
        who  = who
        )
        return redirect("Communication:conversation")
    else:
        return render(request,"Communication/make_call.html",{})

@login_required
def convo_screen(request):
    return render(request,"Communication/convo_screen.html",)

@login_required
def texting_view(request):
    return render(request,"Communication/msg-views.html",)

@method_decorator(login_required,name="dispatch")
class ViewContacts(ListView):
    template_name = "Communication/contacts.html"
    context_object_name = "contacts"
    model = Contacts
    contact = Contacts.objects.all()

@method_decorator(login_required,name="dispatch")
class ViewContact(DetailView):
    template_name = "Communication/view_contact.html"
    context_object_name = "contact"
    model = Contacts

class UpdateContactForm(forms.ModelForm):

    class Meta:
        model = Contacts
        fields = ['contact_name','mobile_number','home_number','work_number','email']

@method_decorator(login_required,name="dispatch")
class UpdateContact(LoginRequiredMixin, UserPassesTestMixin,UpdateView):
    form_class = UpdateContactForm
    template_name = "Communication/update_contact.html"
    context_object_name = "contact"
    model = Contacts

    def form_valid(self,form):
        form.instance.Your_Username= self.request.user.username
        return super().form_valid(form)

    def test_func(self):
        contact = self.get_object()
        if str(self.request.user.username)==str(contact.Whos_Phone):
            return True
        return False

    def get_success_url(self):
        return reverse("Communication:contacts")

@login_required
def DeleteView(request,contact_name,pk):
    name = Contacts.objects.filter(id=pk).get().contact_name
    obj = get_object_or_404(Contacts,id=pk,contact_name=name)
    return render(request,"Communication/delete_contact.html",{"contact":obj})

@login_required
def delete(request,contact_name,pk):
    name = Contacts.objects.filter(id=pk).get().contact_name
    obj = get_object_or_404(Contacts,id=pk,contact_name=name)
    obj.delete()
    return redirect("Communication:contacts")

class CreateContactForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
         self.Whos_Phone1 = kwargs.pop('Whos_Phone1',None)
         super(CreateContactForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Contacts
        fields = ['Whos_Phone','contact_name','mobile_number','home_number','work_number','email']
        required = ('Whos_Phone','contact_name')

        widgets = {
            "Whos_Phone":forms.TextInput(attrs={"required":True,
                                                "placeholder":"Your Username"})
        }
@login_required
def add_contact_view(request):
    form = CreateContactForm()
    return render(request,"Communication/add_contacts.html",{"form":form})

@login_required
def AddContact(request):
    form = CreateContactForm(Whos_Phone1=request.user)
    if request.POST:
        form = CreateContactForm(request.POST)
        if form.is_valid:
            if request.POST['Whos_Phone'] == request.user.username:
                form.save()
                Contacts.objects.filter(Whos_Phone=request.user.username).update(Whos_Phone1=request.user)
                return redirect("Communication:contacts")
            else:
                form = CreateContactForm()
                return render(request,"Communication/bad_name.html")
        else:
            form = CreateContactForm()
            return render(request,"Communication/add_contacts.html",{"form":form})

@method_decorator(login_required, name="dispatch")
class ViewCallLog(ListView):
    model = Call
    template_name = "Communication/call_log.html"
    context_object_name = "call"
    ordering = ['-time']

@method_decorator(login_required, name="dispatch")
class ViewCall(DetailView):
    model = Call
    template_name = "Communication/view_call.html"
    context_object_name = "call"

@login_required
def DeleteLog(request,who,pk):
    name = Call.objects.filter(id=pk).get()
    obj = get_object_or_404(Call,id=pk,who=name.who)
    return render(request,"Communication/deletelog.html",{"call":obj})

@login_required
def deletelog(request,who,pk):
    name = Call.objects.filter(id=pk).get()
    obj = get_object_or_404(Call,id=pk,who=name.who)
    obj.delete()
    return redirect("Communication:call-logs")

@login_required
def voicemail(request):
    return render(request, "Communication/voicemail.html")

@login_required
def text_view(request):
    return render(request,"Communication/text-view.html")

class CreateText(forms.ModelForm):
    class Meta:
        model = Text
        fields = ["texter","who","message"]

        widgets = {
        "texter":forms.TextInput(attrs={"required":True,
                                            "placeholder":"Username"}),
        "who":forms.TextInput(attrs={"required":True,
                                            "placeholder":"Number you want to text"})
        }

@login_required
def send_text_view(request):
    form = CreateText()
    return render(request,"Communication/send-text-view.html",{"form":form})

def counterSubset(list1, list2):
    c1, c2 = Counter(list1), Counter(list2)
    for k, n in c1.items():
        if n > c2[k]:
            return False
    return True

@login_required
def send_text(request):
    form = CreateText()
    if request.POST:
        form = CreateText(request.POST)
        if form.is_valid():
            if request.POST['texter']==request.user.username:
                from twilio.rest import Client
                try:
                    account_sid = TWILIO_AUTH_SID
                    auth_token = TWILIO_AUTH_TOKEN
                    client = Client(account_sid, auth_token)
                    # message = client.messages.create(
                    #     body = request.POST['message'],
                    #     from_="+19564136773",
                    #     to = request.POST['who']
                    #     )
                    # print(message.sid)
                except twilio.base.exceptions.TwilioRestException as e:
                    return render(request,"Communication/bad_number1.html")
                form.save()
                numbers_from = [names for names in list(Text.objects.all().values_list('who'))]
                potential_new_numbers = [numbers for numbers in list(TextSave.objects.filter(sender=request.user.username).all().values_list("target"))]
                #############We were here ###################
                for i, content in enumerate(numbers_from):
                    if request.POST['who'] in content[0]:
                        print("This happened")
                        Text.objects.filter(texter=request.user.username,who=request.POST['who']).update(texter1=request.user)
                        return redirect("Communication:text-section")

                print(content[0])
                print("This also happened")
                for i, content in enumerate(numbers_from):
                     if request.POST['who'] not in content:
                         print("This is happening")
                         TextSave.objects.create(sender1=request.user,
                                             sender=request.user.username,
                                             target=request.POST['who'],
                                             message = request.POST['message'])
                         Text.objects.filter(texter=request.user.username,who=request.POST['who']).update(texter1=request.user)
                         return redirect("Communication:text-section")
            else:
                return render(request,"Communication/bad_name1.html",{"form":form})
        else:
            form = form = CreateText()
            return render(request,"Communication/send-text-view.html",{"form":form})
    else:
        form = form = CreateText()
        return render(request,"Communication/send-text-view.html",{"form":form})

@method_decorator(login_required,name="dispatch")
class Conversations(ListView):
    model = TextSave
    ordering = ["-time"]
    context_object_name = "text"
    template_name = "Communication/view_conversations.html"

@method_decorator(login_required, name="dispatch")
class ViewMessages(ListView):
    model = Text
    template_name = "Communication/view-messages.html"
    context_object_name = "text"
    ordering = ['-time']

@method_decorator(login_required, name="dispatch")
class ViewConversation(DetailView):
    model = Text
    template_name = "Communication/conversation.html"
    context_object_name = "text"

@login_required
def DeleteText(request,who,pk):
    name = Text.objects.filter(id=pk).get()
    obj = get_object_or_404(Text,id=pk,who=name.who)
    return render(request,"Communication/delete_text.html",{"text":obj})

@login_required
def deletetext(request,who,pk):
    name = Text.objects.filter(id=pk).get()
    obj = get_object_or_404(Text,id=pk,who=name.who)
    obj.delete()
    return redirect("Communication:messages")

@login_required
def email_view(request):
    return render(request,"Communication/email-view.html")

class CreateEmail(forms.ModelForm):
    class Meta:
        model = Emailing
        fields = ["username","to","subject","message"]

        widgets = {
        "username":forms.TextInput(attrs={"required":True,
                                            "placeholder":"Your Username"}),
        }

@login_required
def send_email_view(request):
    form = CreateEmail()
    return render(request,"Communication/send-email-view.html",{"form":form})

@login_required
def send_email(request):
    form = CreateText()
    if request.POST:
        form = CreateEmail(request.POST)
        if form.is_valid():
            if request.POST['username']==request.user.username:
                server = smtplib.SMTP('smtp.gmail.com:587')
                context = ssl.create_default_context()
                server.ehlo()
                server.starttls(context=context)
                server.ehlo()
                server.login(settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASSWORD)
                message = "Subject: {}\n\n{}".format(request.POST['subject'],request.POST['message'])
                server.sendmail(settings.EMAIL_HOST_USER,request.POST['to'],message)
                server.quit()
                #send_mail(
                #request.POST['subject'],
                #request.POST['message'],
                #settings.EMAIL_HOST_USER,
                #[receiver_email],
                #)
                form.save()
                Emailing.objects.filter(username=request.user.username,).update(whos_email1=request.user)
                return redirect("Communication:email-section")
            else:
                return render(request,"Communication/bad_name2.html",{"form":form})
        else:
            form  = CreateEmail()
            return render(request,"Communication/send-email-view.html",{"form":form})
    else:
        form = CreateText()
        return render(request,"Communication/send-email-view.html",{"form":form})

@method_decorator(login_required, name="dispatch")
class ViewEmails(ListView):
    model = Emailing
    template_name = "Communication/view-emails.html"
    context_object_name = "email"
    ordering = ['-time']

@method_decorator(login_required, name="dispatch")
class ViewEmailConversation(DetailView):
    model = Emailing
    template_name = "Communication/email-conversation.html"
    context_object_name = "text"

@login_required
def DeleteEmail(request,to,pk):
    name = Emailing.objects.filter(id=pk).get()
    obj = get_object_or_404(Emailing,id=pk,to=name.to)
    return render(request,"Communication/delete_email.html",{"text":obj})

@login_required
def deleteemail(request,to,pk):
    name = Emailing.objects.filter(id=pk).get()
    obj = get_object_or_404(Emailing,id=pk,to=name.to)
    obj.delete()
    return redirect("Communication:emails")
