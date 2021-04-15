from django.shortcuts import render
from .models import SocialMedia
# Create your views here.
def social_media(request):
    return render(request,"Social/social_media.html",{"apps":SocialMedia.objects.all().order_by('name')})
