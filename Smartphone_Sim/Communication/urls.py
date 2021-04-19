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
    path("Call-Section/Delete-Contact/<str:contact_name>/<int:pk>",views.DeleteView,name="delete-contact"),
    path("Call-Section/Delete-Contact/<str:contact_name>/<int:pk>/Deleting",views.delete,name="delete"),
    path("Call-Section/Add-Contact/",views.add_contact_view,name="add-contact-view"),
    path("Call-Section/Add-Contact/Add",views.AddContact,name="add"),
    path("Call-Section/Call-Log/",views.ViewCallLog.as_view(),name="call-logs"),
    path("Call-Section/Call-Log/<str:who>/<int:pk>/",views.ViewCall.as_view(),name="call-log"),
    path("Call-Section/Call-Log/Delete/<str:who>/<int:pk>/",views.DeleteLog,name="ask-delete-log"),
    path("Call-Section/Call-Log/Delete/<str:who>/<int:pk>/Deleting",views.deletelog,name="delete-log"),
    path("Call-Section/Voice-Mail/",views.voicemail,name="voicemail"),
    path("Text-Section/",views.text_view,name="text-section"),
    path("Text-Section/Send-Text/",views.send_text_view,name="send-text-view"),
    path("Text-Section/Send-Text/Sending",views.send_text,name="send-text")
]
