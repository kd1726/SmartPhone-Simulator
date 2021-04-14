from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.
class Call(models.Model):
    caller = models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    who = models.CharField(max_length=50,null=True)
    time = models.DateTimeField(default = timezone.now)
    app_img = models.ImageField(upload_to="static/Images",default="static/Call.png")

    def __str__(self):
        return f"Called {who} at {time}"

class Text(models.Model):
    texter = models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    who = models.CharField(max_length=50,null=True)
    message = models.TextField(max_length=1000,null=False)
    time = models.DateTimeField(default = timezone.now)
    app_img = models.ImageField(upload_to="static/Images",default="static/Text.png")
    def __str__(self):
        i =0
        prev = ""
        while i<50:
            prev+=message[i]
            i+=1
        return f"{prev} <--> {time}"
