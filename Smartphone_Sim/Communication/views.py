from django.shortcuts import render,redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Contacts
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
                                to=request.POST['number'],
                                from_='+12188750645')
        print(call.sid)
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
def deleting(request):
    return render(request,"Communication:delete_contact.html")

@method_decorator(login_required,name="dispatch")
class DeleteContact(LoginRequiredMixin, UserPassesTestMixin,DeleteView):
    model = Contacts
    template_name = "Communication/delete_contact.html"
    context_object_name = "contact"

    def test_func(self):
        contact = self.get_object()
        if str(self.request.user) ==str(contact.Whos_Phone):
            return True
        return False

    def get_success_url(self):
        return reverse('Communication:contacts')
