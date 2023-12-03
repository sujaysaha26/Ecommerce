from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


# Create your views here.

def index(request):
    return render(request, 'index.html')

def handleSignup(request):
    if request.method == "POST":
        # Get the post parameters
        username = request.POST['username']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        email = request.POST['email']

        if pass1==pass2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username already taken')
                return redirect('/')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email has been taken')
                return redirect('/')
            else:
                user = User.objects.create_user(username=username, password=pass1, email=email)
                user.save()
                print('User creaated')
                messages.success(request, 'Your account has been created successfully, please try to login now.')
                return redirect('/')
        else:
            messages.error(request, 'password not matching.')
            return redirect('/')
    else:
        return render(request, 'login.html')


def logintemp(request):
    return render(request, 'login.html')

def handleLogin(request):
    if request.method == "POST":
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']
        user = auth.authenticate(username=loginusername, password=loginpassword)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You have been successfully logged in.')
            return redirect('/')
        else:
            messages.error(request, 'Invalid username or password, please check again and try it.')
            return redirect('/')
    else:
        return render(request, 'login.html')


def handleLogout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('/')
