from django.shortcuts import render, HttpResponseRedirect
from user.forms import UserLoginForm, UserRegisterForm, UserProfileForm
from user.models import Users
from django.contrib import auth, messages
from django.urls import reverse


def email_verification(request):
    return render(request, 'user/email_verification.html')


def login(request):
    if request.method == "POST":
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                messages.success(request, 'Авторизация прошла успешно')
                return HttpResponseRedirect(reverse('index'))
    else:
        form = UserLoginForm()
    context = {'form': form}
    return render(request, 'user/login.html', context)


def profile(request):
    if request.method == "POST":
        form = UserProfileForm(instance=request.user, data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Профиль обновлен')
            return HttpResponseRedirect(reverse('user:profile'))
    else:
        form = UserProfileForm(instance=request.user)
    context = {'title': 'Store - Профиль', "form": form}
    return render(request, 'user/profile.html', context)


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Регистрация прошла успешно!')
            return HttpResponseRedirect(reverse('user:login'))
        else:
            print(form.errors)
    else:
        form = UserRegisterForm()
    context = {"form": UserRegisterForm()}
    return render(request, 'user/register.html', context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))