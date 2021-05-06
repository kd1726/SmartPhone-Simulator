from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Contacts,Call,Text,TextSave,Emailing,ReceivedTexts
from django.contrib.auth.models import User
from django.views.generic import ListView,CreateView,UpdateView,DeleteView,DetailView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import os
from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse
from Smartphone_sim.settings import TWILIO_AUTH_SID, TWILIO_AUTH_TOKEN, TWILIO_API_SID, TWILIO_APP_SID, TWILIO_API_SECRET_KEY
from twilio.jwt.access_token import AccessToken
from twilio.jwt.access_token.grants import VoiceGrant
from twilio.twiml.voice_response import VoiceResponse, Dial
from dotenv import load_dotenv
from django.conf import settings
from django import forms
from itertools import chain
from django.db.models import CharField
import twilio
from twilio import twiml
from twilio.twiml.messaging_response import MessagingResponse
import smtplib, ssl
from django_api_forms import Form
from collections import Counter
import pprint as p
# Create your views here.
@csrf_exempt
def sms_response(request):
    number = request.POST['From']
    body = request.POST['Body'].lower()
    fake_list_of_usernames = User.objects.all().values_list('username')
    list_of_usernames = [content[0] for i,content in enumerate(fake_list_of_usernames)]
    numbers_from = [names for names in list(TextSave.objects.all().values_list('target'))]
    numbers_from1 = [names for names in list(ReceivedTexts.objects.all().values_list('sender'))]
    users = [users for users in list(User.objects.all())]
    who = ''
    print(list_of_usernames)
    print(users)
    for i in range(len(body)+1):
        if who[1:] in list_of_usernames:
            if number[2:] not in numbers_from:
                for i in users:
                    if i.username==who[1:]:
                        print(i.username)
                        TextSave.objects.create(sender1=i,
                                            sender=who[1:],
                                            target=number[2:],
                                            message = body[len(who)+1:])

                        ReceivedTexts.objects.create(message = body[len(who)+1:],
                                                sender = number[2:],
                                                to = who[1:])

                        return HttpResponse(str(body))
            else:
                ReceivedTexts.objects.create(message = body[len(who)+1:],
                                        sender = number[2:],
                                        to = who[1:])

                return HttpResponse(str(body))

        who+=body[i]

        if i==50 and who not in list_of_usernames:
            resp = MessagingResponse()
            resp.message("You did not input a valid username. Please Try again!")
            return HttpResponse(str(resp))

        elif "@"!=body[0]:
            resp = MessagingResponse()
            resp.message("You did not add an initiator. Please add '@' before sending your text!")
            return HttpResponse(str(resp))
        else:
            pass
@login_required
def communcation_view(request):
    return render(request,"Communication/communication.html",{})

@login_required
def call_view(request):
    return render(request,"Communication/Call_View.html",{})

@login_required
@csrf_exempt
def make_a_call_view(request):
    return render(request,"Communication/make_call.html",{})

def get_token(request):
    identity = '+19564136773'
    outgoing_app_sid = TWILIO_APP_SID

    access_token = AccessToken(TWILIO_AUTH_SID,TWILIO_API_SID,
                                TWILIO_API_SECRET_KEY,identity=identity)
    voice_grant = VoiceGrant(
        outgoing_application_sid=outgoing_app_sid,
        incoming_allow=False,
    )
    access_token.add_grant(voice_grant)

    response = JsonResponse(
        {'token':access_token.to_jwt().decode(),'identity': identity})

    return response

@login_required
@csrf_exempt
def calling(request):
    request.method == "POST"
    if request.POST:
        print("Hello is this being invoked?")
        # try:
        #     account_sid = TWILIO_AUTH_SID
        #     auth_token = TWILIO_AUTH_TOKEN
        #     client = Client(account_sid, auth_token)
        #
        #     call = client.calls.create(
        #                             url='http://demo.twilio.com/docs/voice.xml',
        #                             to=number,
        #                             from_='+19564136773')
        #
        #     print(call.sid)
        # except twilio.base.exceptions.TwilioRestException as e:
        #     return render(request, "Communication/bad_number.html")
        # try:
        #     numbers = Contacts.objects.all().filter(Whos_Phone=request.user.username, mobile_number = number).get()
        #     print(numbers.contact_name)
        #     if numbers!= None:
        #         who = numbers.contact_name
        #     else:
        #         who = number
        # except Contacts.DoesNotExist as e:
        #     who = number
        p.pprint(request.POST)
        response = VoiceResponse()
        dial = Dial(callerId='+19564136773')
#####################Was here last time############################
        if 'To' in request.POST and request.POST['To'] != '+19564136773':
            print('outbound call')
            dial.number(request.POST['To'])
            str(response.append(dial))
            return redirect("Communication:make-call")
    return ''
    #return None
        #return redirect("Communication:make-call")
        # Call.objects.create(
        # caller1 = request.user,
        # caller = request.user.username,
        # who  = number
        # )
        # return redirect("Communication:conversation")


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
                    message = client.messages.create(
                        body = request.POST['message'],
                        from_="+19564136773",
                        to = request.POST['who']
                        )
                    print(message.sid)
                except twilio.base.exceptions.TwilioRestException as e:
                    return render(request,"Communication/bad_number1.html")
                numbers_from = [names for names in list(Text.objects.all().values_list('who'))]
                potential_new_numbers = [numbers for numbers in list(TextSave.objects.filter(sender=request.user.username).all().values_list("target"))]
                nums = [content[0] for i, content in enumerate(numbers_from)]
                print(nums)
                for i in nums:
                    if request.POST['who'] in nums:
                        print(i)
                        print("This happened")
                        form.save()
                        Text.objects.filter(texter=request.user.username,who=request.POST['who']).update(texter1=request.user)
                        return redirect("Communication:text-section")
                print("This also happened")
                for i in nums:
                     if request.POST['who'] not in nums:
                         print("This is happening")
                         TextSave.objects.create(sender1=request.user,
                                             sender=request.user.username,
                                             target=request.POST['who'],
                                             message = request.POST['message'])
                         form.save()
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

@login_required
def specific_converseration(request,who,pk):
    sent_texts = Text.objects.filter(texter=request.user.username,who=who).all()
    recieved = ReceivedTexts.objects.filter(sender=who,to=request.user.username).all()
    my_objs = sorted(chain(sent_texts,recieved),key=lambda obj: obj.time)
    print(my_objs)
    return render(request,"Communication/text_conversation.html",{"texts":my_objs,
                                                                    "the_number":who,
                                                                    "the_id":pk})

@login_required
def sent_another_text(request,who,pk):
    if request.POST:
        try:
            account_sid = TWILIO_AUTH_SID
            auth_token = TWILIO_AUTH_TOKEN
            client = Client(account_sid, auth_token)
            message = client.messages.create(
                body = request.POST['message'],
                from_="+19564136773",
                to = who
                )
            print(message.sid)
        except twilio.base.exceptions.TwilioRestException as e:
            return render(request,"Communication/bad_number1.html")
        Text.objects.create(texter1=request.user,texter=request.user.username,
                            who=who,message=request.POST['message'])
        print("Work until here")
        return redirect("Communication:specific-convo",who,pk)

@login_required
def delete_text_conversation_view(request,who,username,pk):
    obj = get_object_or_404(TextSave,sender=username,target=who,id=pk)
    print(obj)
    return render(request,"Communication/delete-text-conversation.html",{"convo":obj})

@login_required
def delete_text_conversation(request,who,username,pk):
    obj = get_object_or_404(TextSave,sender=username,target=who,id=pk)
    obj.delete()
    return redirect("Communication:Conversations")

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
