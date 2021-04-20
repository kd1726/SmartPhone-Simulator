from django.shortcuts import render

# Create your views here.
def game_center(request):
    return render(request,"Games/game_center.html")

def blackjack_ask(request):
    return render(request,"Games/bjask.html")

def play_blackjack_single(request):
    return render(request,"Games/bjsingle.html")

def play_blackjack_double(request):
    return render(request,"Games/bjdouble.html")

def rock_paper_scissor(request):
    return render(request,"Games/rps.html")

def guess_the_number(request):
    return render(request,"Games/guess.html")

def tic_tac_toe(request):
    return render(request,"Games/ttt.html")
