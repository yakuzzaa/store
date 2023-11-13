from django.shortcuts import render, HttpResponseRedirect
from user.forms import UserLoginForm, UserRegisterForm, UserProfileForm
from user.models import Users
from django.contrib.auth.views import LoginView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse, reverse_lazy
from products.models import Basket

from common.views import TitleMixin


def email_verification(request):
    return render(request, 'user/email_verification.html')


class UserLoginView(SuccessMessageMixin, LoginView):
    template_name = 'user/login.html'
    form_class = UserLoginForm
    reverse_lazy = 'index'
    success_message = 'Авторизация прошла успешно!'


class UserRegistrationView(TitleMixin, SuccessMessageMixin, CreateView):
    model = Users
    template_name = 'user/register.html'
    form_class = UserRegisterForm
    success_url = reverse_lazy('user:login')
    success_message = 'Регистрация прошла успешно!'
    title = 'Store - Регистрация'


class UserProfileView(TitleMixin, UpdateView):
    model = Users
    template_name = 'user/profile.html'
    form_class = UserRegisterForm
    title = 'Store - Профиль'

    def get_success_url(self):
        return reverse_lazy('user/profile.html', args=(self.object.id,))
