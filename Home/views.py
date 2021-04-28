from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import MakeAccount
# Create your views here.

def Login_View(request):
    return render(request,"Home.html",{})

def Make_Your_Account(request):
    form = MakeAccount()
    if request.POST:
        form =MakeAccount(request.POST)
        print(form.errors)
        if form.is_valid():
            form.save()
            return redirect("Created")
        else:
            form = MakeAccount()
            return render(request,"Make_Account.html",{"form":form,"errors":form.errors})
    return render(request,"Make_Account.html",{"form":form})

def Account_Created(request):
    return render(request,"Account_Created.html",{})

def Account_Not_Created(request):
    form =MakeAccount(request.POST)
    print(form.errors)
    return render(request,"Account_Not_Created.html",{})

@login_required
def Home(request):
    return render(request,"Home_Page.html",{})
