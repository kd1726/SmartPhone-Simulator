from django.urls import path
from . import views
app_name="Miscellaneous"

urlpatterns = [
    path("",views.tool_view,name="tool-view"),
    path("Profile/<str:username>/<int:pk>/",views.profile,name="profile"),
    path("Profile/Delete/<str:username>/<int:pk>/",views.delete_user_view,name="delete-user"),
    path("Profile/Delete/Deleting/<str:username>/<int:pk>/",views.delete_user,name="deleting-user"),
    path("Translator/",views.translation_view,name="translate-view"),
    path("Translator/Translate",views.translate_form_view,name="translate-form-view"),
    path("Translator/Translate/Translating/",views.translate,name="translating"),
    path("Translator/Translate/Translated/<str:orgin_language>/<str:new_language>/<int:pk>/",views.translated,name="translated"),
    path("Translator/Logs/",views.ViewTranslationLogs.as_view(),name="t-logs"),
    path("Translator/Logs/Log/<str:orgin_language>/<str:new_language>/<int:pk>/",views.ViewTranslationLog.as_view(),name="view-t-logs"),
    path("Translator/Logs/Log/Delete/<str:orgin_language>/<str:new_language>/<int:pk>/",views.DeleteTLog,name="delete-view-t-logs"),
    path("Translator/Logs/Log/Delete/Deleting/<str:orgin_language>/<str:new_language>/<int:pk>/",views.deletetlog,name="deleting-t-log"),
    path("Currency-Converter/",views.cc,name="cc"),
    path("Maps/",views.maps,name="maps"),
    path("Weather/",views.weather,name="weather"),
    path("Authenticator/",views.auth,name="auth"),
    path("Picutres-Images/",views.pi,name="pi"),
]
