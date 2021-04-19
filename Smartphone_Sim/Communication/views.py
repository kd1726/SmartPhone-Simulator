from django.shortcuts import render,redirect,get_object_or_404
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Contacts,Call,Text
from django.contrib.auth.models import User
from django.views.generic import ListView,CreateView,UpdateView,DeleteView,DetailView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
import os
from twilio.rest import Client
from Smartphone_Sim.settings import TWILIO_AUTH_SID, TWILIO_AUTH_TOKEN
from django import forms
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
    import twilio
    if request.POST:
        global number
        number = request.POST['number']
        account_sid = TWILIO_AUTH_SID
        auth_token = TWILIO_AUTH_TOKEN
        client = Client(account_sid, auth_token)

        call = client.calls.create(
                                url='http://demo.twilio.com/docs/voice.xml',
                                to=number,
                                from_='+12188750645')
        print(call.sid)
        #numbers = Contacts.objects.all().filter(Whos_Phone=request.user.username)
        #for i in numbers:
        #    if i.mobile_number==number:
        #        who = Contacts.objects.all().filter(Whos_Phone=request.user.username,mobile_number=number).contact_name
        #        break
        #    else:
        #        who = number
        Call.objects.create(
        caller1 = request.user,
        caller = request.user.username,
        who  = number
        )
        return reverse("Communication:conversation")
    else:
        return render(request,"Communication/make_call.html",{})

@login_required
def convo_screen(request):
    return render(request,"Communication/convo_screen.html",)

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

@login_required
def send_text(request):
    form = CreateText()
    if request.POST:
        form = CreateText(request.POST)
        if form.is_valid():
            if request.POST['texter']==request.user.username:
                from twilio.rest import Client
                account_sid = TWILIO_AUTH_SID
                auth_token = TWILIO_AUTH_TOKEN
                client = Client(account_sid, auth_token)
                print(dir(client))
                message = client.messages.create(
                    body = str(request.POST['message']),
                    from_="+12188750645",
                    to = str(request.POST['who'])
                    )
                print(message.sid)
                form.save()
                return redirect("Communication:text-section")
            else:
                return render(request,"Communication/bad_name1.html",{"form":form})
        else:
            form = form = CreateText()
            return render(request,"Communication/send-text-view.html",{"form":form})
    else:
        form = form = CreateText()
        return render(request,"Communication/send-text-view.html",{"form":form})
