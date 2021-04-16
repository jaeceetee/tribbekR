from django.urls import path
from django.conf.urls.static import static
from django.conf.urls import url
from .views import host_screen, play_game, user_list, player
from . import views


app_name = "trivia"

urlpatterns = [
    path('create_game/', views.create_game, name="create_game"), # Needs to be on top
    path('play_game/', views.play_game, name="play_game"),

    path('<int:game_num>/host_screen', host_screen, name="host"),
    path('<int:game_num>/player_screen', views.player, name="player"),
    
    #path('', "/Users/Login", name="login"),
    path('<str:room_name>/<int:question_num>/', views.question, name="questions"),
    
    path('question/<int:question_num>', views.nextQuestion, name='nextQuestion'),
    url(r'^$', user_list, name='user_list'),


]