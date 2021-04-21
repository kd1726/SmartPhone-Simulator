from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView, DetailView,DeleteView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django import forms
# Create your views here.

@login_required
def tool_view(request):
    return render(request,"Miscellaneous/tools.html")

@login_required
def profile(request,username,pk):
    return render(request,"Miscellaneous/profile.html")

@login_required
def delete_user_view(request,username,pk):
    return render(request, "Miscellaneous/delete_user.html")

def delete_user(request,username,pk):
    if request.POST:
        user = User.objects.filter(username = username, id =pk).get()
        user.delete()
        return redirect("Login")
    else:
        return render(request, "Miscellaneous/delete_user.html")

@login_required
def translation_view(request):
    return render(request,"Miscellaneous/translator.html")
