"""Smartphone_Simulator URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings
from Home import views
from Communication import views as vc
urlpatterns = [
    path("",auth_views.LoginView.as_view(template_name ="Home.html"),name = "Login"),
    path("Logout/",auth_views.LogoutView.as_view(template_name="Home.html"),name="Logout"),
    path("Create-User/",views.Make_Your_Account,name="Make-User"),
    path("Create-User/Validated/",views.Account_Created,name="Created"),
    path("Create-User/Invalid/",views.Account_Not_Created,name="Invalidated"),
    path("Home/",views.Home,name="Home"),
    path("Communication/",include("Communication.urls",namespace="Communication")),
    path("Social-Media/",include("Social_Media.urls",namespace="Social")),
    path("Games/",include("Games.urls",namespace="Games")),
    path("Miscellaneous/",include("Miscellaneous.urls",namespace="Tools")),
    path('admin/', admin.site.urls),
]
#+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
