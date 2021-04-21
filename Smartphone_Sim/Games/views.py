from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def game_center(request):
    return render(request,"Games/game_center.html")

@login_required
def blackjack_ask(request):
    return render(request,"Games/bjask.html")

@login_required
def play_blackjack_single(request):
    return render(request,"Games/bjsingle.html")

@login_required
def play_blackjack_double(request):
    return render(request,"Games/bjdouble.html")

@login_required
def rock_paper_scissor(request):
    return render(request,"Games/rps.html")

@login_required
def guess_the_number(request):
    return render(request,"Games/guess.html")

@login_required
def tic_tac_toe(request):
    return render(request,"Games/ttt.html")
