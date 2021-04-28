from django.shortcuts import render, redirect,reverse, HttpResponseRedirect, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DetailView,DeleteView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django import forms
from .models import Translator
from translate import Translator as tr
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

@login_required
def delete_user(request,username,pk):
    if request.POST:
        obj = get_object_or_404(User, username = request.user.username, id =request.user.id)
        print(obj.username)
        obj.delete()
        return redirect("Login")
    else:
        return render(request, "Miscellaneous/delete_user.html")

@login_required
def translation_view(request):
    return render(request,"Miscellaneous/translator.html")

class TranslateForm(forms.ModelForm):
    class Meta:
        model = Translator
        fields = ['username','orgin_language','new_language','text_to_translate']
        widgets = {
        'username': forms.TextInput(attrs={"required":True}),
        "text_to_translate":forms.Textarea(attrs={
                                        "required":True,
                                        "placeholder":"Max of 1000 characters",
                                        "rows":5,
                                        "cols":50})
                                        }

@login_required
def translate_form_view(request):
    form = TranslateForm()
    return render(request,"Miscellaneous/translate.html",{"form":form})

def translate(request):
    form = TranslateForm()
    if request.POST:
        form = TranslateForm(request.POST)
        if form.is_valid():
            if request.POST['username']==request.user.username:
                ol = request.POST['orgin_language']
                nl = request.POST['new_language']
                tot = request.POST['text_to_translate']
                translator = tr(from_lang = ol, to_lang = nl)
                translation = translator.translate(tot)
                message = f"{ol} IS AN INVALID SOURCE LANGUAGE . EXAMPLE: LANGPAIR=EN|IT USING 2 LETTER ISO OR RFC3066 LIKE ZH-CN. ALMOST ALL LANGUAGES SUPPORTED BUT SOME MAY HAVE NO CONTENT"
                message1 =f"{nl} IS AN INVALID SOURCE LANGUAGE . EXAMPLE: LANGPAIR=EN|IT USING 2 LETTER ISO OR RFC3066 LIKE ZH-CN. ALMOST ALL LANGUAGES SUPPORTED BUT SOME MAY HAVE NO CONTENT"
                if message == translation:
                    return render(request,"Miscellaneous/bad_lang.html")
                elif message1 == translation:
                    return render(request,"Miscellaneous/bad_lang.html")
                else:
                    new_obj = Translator.objects.create(owner= request.user, username = request.user.username, orgin_language = ol,
                                                new_language = nl, text_to_translate = tot, translation = translation)
                    id = new_obj.id
                    return redirect("Tools:translated",orgin_language=ol, new_language=nl,pk=id)
            else:
                return render(request,"Miscellaneous/bad_name3.html")
        else:
            form = TranslateForm()
            return render(request,"Miscellaneous/translate.html",{"form":form})
    else:
        form = TranslateForm()
        return render(request,"Miscellaneous/translate.html",{"form":form})

@login_required
def translated(request,orgin_language,new_language,pk):
    obj = Translator.objects.filter(id=pk,orgin_language=orgin_language,new_language=new_language).get()
    return render(request, "Miscellaneous/translated.html",{"result":obj})

@method_decorator(login_required,name="dispatch")
class ViewTranslationLogs(ListView):
    template_name = "Miscellaneous/t-logs.html"
    model = Translator
    context_object_name="translated"
    ordering=['-time']

@method_decorator(login_required,name="dispatch")
class ViewTranslationLog(DetailView):
    template_name = "Miscellaneous/view_t-log.html"
    model = Translator
    context_object_name="translated"


@login_required
def DeleteTLog(request,orgin_language,new_language,pk):
    obj = get_object_or_404(Translator,id=pk,orgin_language=orgin_language, new_language= new_language)
    return render(request,"Miscellaneous/delete_t_log.html",{"translated":obj})

@login_required
def deletetlog(request,orgin_language,new_language,pk):
    obj = get_object_or_404(Translator,id=pk,orgin_language=orgin_language, new_language= new_language)
    obj.delete()
    return redirect("Tools:t-logs")

@login_required
def cc(request):
    return render(request,"Miscellaneous/cc.html")

@login_required
def maps(request):
    return render(request,"Miscellaneous/maps.html")

@login_required
def weather(request):
    return render(request,"Miscellaneous/weather.html")

@login_required
def auth(request):
    return render(request,"Miscellaneous/auth.html")

@login_required
def pi(request):
    return render(request,"Miscellaneous/images.html")
