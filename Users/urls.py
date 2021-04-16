from django.urls import path
from . import views

app_name = "Users"

urlpatterns = [
    path('', views.index, name="index"),
    path('register/', views.register_user, name="register"),
    path('login/', views.login_user, name="login"),
    path('user_home', views.user_home, name="user_home"),
    path('logout/', views.logout_user, name="logout"),
]