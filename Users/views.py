from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.http.response import HttpResponseRedirect
from django.urls.base import reverse

# Register User - Host
def register_user(request):
    if request.method == "POST":
        form = request.POST 
        username = form['username']
        email = form['email']
        password = form['password']

        if not User.objects.filter(username=username).exists():
            user = User()
            user.username = username
            user.email = email
            user.set_password(password)
            user.save()

            login(request, user)

            return HttpResponseRedirect(reverse('Users.register'))
        else:
            print("Username has been taken! Try a new username!")
    return render(request, 'Users/register.html')

def login_user(request):
    if request.method == "POST":
        form = request.POST
        username = form['username']
        password = form['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            print('logging in user')
            login(request, user)
            return HttpResponseRedirect(reverse('Users:user_home'))

    return render(request, 'Users/login.html')

def user_home(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('Users:login'))


    return render(request, 'Users/user_home.html')

def index(request):
    return render(request, "Users/login.html")