from django.urls import path
from . import views
app_name = "Social_Media"

urlpatterns=[
    path("",views.social_media,name="social_media")
]
