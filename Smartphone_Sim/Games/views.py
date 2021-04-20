from django.shortcuts import render

# Create your views here.
def game_center(request):
    return render(request,"Games/game_center.html")
