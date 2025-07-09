from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
# for login session cookie
from django.contrib.auth import login
# for error handling
from django.db import IntegrityError
# from django.core.exceptions import ValidationError

# Create your views here.


def home(request):
    return render(request, 'tasks/index.html')


def signup(request):
    if request.method == 'GET':
        return render(request, 'tasks/signup.html', {
            'form': UserCreationForm,
        })
    else:

        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                    username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return render(request, 'tasks/signup.html', {
                    'form': UserCreationForm,
                    'error': "User Created Successfully"
                })
            except IntegrityError:
                return render(request, 'tasks/signup.html', {
                    'form': UserCreationForm,
                    'error': "Username is already in use"
                })

        return render(request, 'tasks/signup.html', {
            'form': UserCreationForm,
            'error': "Password do not match"
        })


def tasks(request):
    return render(request, 'tasks/tasks.html')


# def log_in(request):
#     return render(request, 'accounts/login')


def profile(request):
    return render(request, 'account/profile.html', {})
