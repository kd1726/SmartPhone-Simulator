from django.urls import path
from . import views
app_name="Miscellaneous"

urlpatterns = [
    path("",views.tool_view,name="tool-view"),
    path("Profile/<str:username>/<int:pk>/",views.profile,name="profile"),
    path("Profile/Delete/<str:username>/<int:pk>/",views.delete_user_view,name="delete-user"),
    path("Profile/Delete/Deleting/<str:username>/<int:pk>/",views.delete_user,name="deleting-user"),
    path("Translator/",views.translation_view,name="translate-view")
]
