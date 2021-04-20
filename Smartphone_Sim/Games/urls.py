from django.urls import path
from . import views
app_name="Games"

urlpatterns = [
    path("",views.game_center,name="game-center"),
    path("Black-Jack-Mode/",views.blackjack_ask,name="black-jack-ask"),
    path("Black-Jack-Single/",views.play_blackjack_single,name="black-jack-single"),
    path("Black-Jack-Double/",views.play_blackjack_double,name="black-jack-double")
]
