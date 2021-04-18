from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Contacts
from django.contrib.auth.models import User
from django.views.generic import ListView,CreateView,UpdateView,DeleteView,DetailView
import os
from twilio.rest import Client
from Smartphone_Sim.settings import TWILIO_AUTH_SID, TWILIO_AUTH_TOKEN
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
    try:
        if request.POST:
            number = request.POST['number']
            account_sid = TWILIO_AUTH_SID
            auth_token = TWILIO_AUTH_TOKEN
            client = Client(account_sid, auth_token)

            call = client.calls.create(
                                    url='http://demo.twilio.com/docs/voice.xml',
                                    to=request.POST['number'],
                                    from_='+12188750645'
                        )

            print(call.sid)
    except IndexError as e:
        pass
@login_required
def certify_call(request):
    return render(request,"Communication/calling.html",)

@method_decorator(login_required,name="dispatch")
class ViewContacts(ListView):
    template_name = "Communication/contacts.html"
    context_object_name = "contacts"
    model = Contacts
    contact = Contacts.objects.all()
