from django.shortcuts import render
from user.forms import UserLoginForm
from  user.models import Users


def email_verification(request):
    return render(request, 'user/email_verification.html')


def login(request):
    context = {'form': UserLoginForm()}
    return render(request, 'user/login.html', context)


def profile(request):
    return render(request, 'user/profile.html')


def register(request):
    return render(request, 'user/register.html')
