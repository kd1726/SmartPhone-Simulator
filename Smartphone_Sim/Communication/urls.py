from django.urls import path
from . import views
app_name="Communication"

urlpatterns=[
    path("",views.communcation_view,name="communication-view"),
    path("Call-Section/",views.call_view,name="call-view"),
    path("Call-Section/Make-Call/",views.make_a_call_view,name="make-call"),
    path("Call-Section/Make-Call/Calling",views.calling,name="calling"),
    path("Call-Section/Make-Call/talking/<str:number>/",views.convo_screen,name="conversation"),
    path("View-Contacts/",views.ViewContacts.as_view(),name="contacts"),
    #path("View-Contacts/<str:contact_name>/<int:pk>")
]
