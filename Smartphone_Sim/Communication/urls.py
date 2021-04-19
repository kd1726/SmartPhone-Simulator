from django.urls import path
from . import views
app_name="Communication"

urlpatterns=[
    path("",views.communcation_view,name="communication-view"),
    path("Call-Section/",views.call_view,name="call-view"),
    path("Call-Section/Make-Call/",views.make_a_call_view,name="make-call"),
    path("Call-Section/Make-Call/Calling",views.calling,name="calling"),
    path("Call-Section/Make-Call/Calling/talking/",views.convo_screen,name="conversation"),
    path("Call-Section/View-Contacts/",views.ViewContacts.as_view(),name="contacts"),
    path("Call-Section/View-Contacts/<str:contact_name>/<int:pk>",views.ViewContact.as_view(),name="view-contact"),
    path("Call-Section/Update-Contact/<str:contact_name>/<int:pk>",views.UpdateContact.as_view(),name="update-contact"),
    path("Call-Section/Delete-Contact/<str:contact_name>/<int:pk>",views.DeleteContact.as_view(),name="delete-contact")
    #path("View-Contacts/<str:contact_name>/<int:pk>")
]
