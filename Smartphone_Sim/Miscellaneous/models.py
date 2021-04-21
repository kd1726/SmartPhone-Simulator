from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Translator(models.Model):
    owner = models.ForeignKey(User,on_delete=models.CASCADE)
    username = models.CharField(max_length = 50, blank=False, null=True)
    text_to_translate = models.TextField(max_length=1000, blank = False, null=True)
    translation = models.TextField(max_length=1000, blank = False, null=True)

    def __str__(self):
        return f"{username}'s Translation'"
