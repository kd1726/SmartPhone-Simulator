from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.
class Call(models.Model):
    caller1 = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    caller = models.CharField(max_length=50,null=True, blank = True)
    who = models.CharField(max_length=50,null=True)
    time = models.DateTimeField(default = timezone.now)
    def __str__(self):
        return f"Called {self.who} at {self.time}"

class Text(models.Model):
    texter1 = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    texter = models.CharField(max_length=50,null=True, blank = True)
    who = models.CharField(max_length=50,null=True)
    message = models.TextField(max_length=1000,null=False)
    time = models.DateTimeField(default = timezone.now)
    def __str__(self):
        return f"{self.texter} --> {self.who}"

class ReceivedTexts(models.Model):
    message = models.TextField(max_length=1000,null=False)
    time = models.DateTimeField(default = timezone.now)
    sender = models.CharField(max_length=50,null=True, blank = True)
    to = models.CharField(max_length=50,null=True, blank = True)
    def __str__(self):
        return f"{self.sender}-->{self.to}"
        
class TextSave(models.Model):
    sender1 = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    sender =  models.CharField(max_length=50,null=True, blank = True)
    target = models.CharField(max_length=50,null=True)
    message = models.TextField(max_length=1000,null=False)
    time = models.DateTimeField(default = timezone.now)
    def __str__(self):
        return f"{self.sender} <--> {self.target}"
    # texter1 = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    # # def __str__(self):
    # #     return f"{self.texter}<-->{self.who}"

class Contacts(models.Model):
    Whos_Phone = models.CharField(max_length=50,null=True, blank = True)
    Whos_Phone1 = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    contact_name = models.CharField(max_length=50,null=True, blank = True)
    mobile_number = models.CharField(max_length=18,null=True,blank = True)
    home_number = models.CharField(max_length=18,default="#")
    work_number = models.CharField(max_length=18,default="#")
    email = models.CharField(max_length=20,default="#")

    def __str__(self):
        return self.contact_name

class Emailing(models.Model):
    whos_email1 = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    username = models.CharField(max_length=50,null=True, blank = True)
    to =  models.EmailField(max_length=50,null=True, blank = True)
    subject =  models.CharField(max_length=50,null=True)
    message = models.TextField(max_length=1000,null=False)
    time = models.DateTimeField(default = timezone.now)

    def __str__(self):
        return self.to
