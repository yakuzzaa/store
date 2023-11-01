from django.shortcuts import render


def email_verification(request):
    return render(request, 'user/email_verification.html')


def login(request):
    return render(request, 'user/login.html')


def profile(request):
    return render(request, 'user/profile.html')


def register(request):
    return render(request, 'user/register.html')
