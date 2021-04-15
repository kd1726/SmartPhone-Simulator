from django.db import models

# Create your models here.
class SocialMedia(models.Model):
    name = models.CharField(max_length=20,null=True)
    app_img = models.FilePathField(path="static/social-media-images",default=None)
    link = models.CharField(max_length=200,null=True)

    def __str__(self):
        return f"{self.name}"
