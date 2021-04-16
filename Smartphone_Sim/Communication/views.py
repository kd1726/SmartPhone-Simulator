from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Contacts
from django.contrib.auth.models import User
from django.views.generic import ListView,CreateView,UpdateView,DeleteView,DetailView
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

@method_decorator(login_required,name="dispatch")
class ViewContacts(ListView):
    template_name = "Communication/contacts.html"
    context_object_name = "contacts"
    model = Contacts
    contact = Contacts.objects.all()
