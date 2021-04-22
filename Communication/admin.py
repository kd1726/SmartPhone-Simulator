from django.contrib import admin
from .models import Call, Text, Contacts,Emailing
# Register your models here.
admin.site.register(Call)
admin.site.register(Text)
admin.site.register(Contacts)
admin.site.register(Emailing)
