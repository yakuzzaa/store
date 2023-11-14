from django.http import HttpResponseRedirect
from django.views.generic import TemplateView

from user.forms import UserLoginForm, UserRegisterForm
from user.models import Users, EmailVerification
from django.contrib.auth.views import LoginView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy, reverse

from common.views import TitleMixin


class UserLoginView(TitleMixin,SuccessMessageMixin, LoginView):
    model = Users
    template_name = 'user/login.html'
    title = "DeadStore|Авторизация"
    form_class = UserLoginForm
    success_url = reverse_lazy('index')
    success_message = 'Авторизация прошла успешно!'


class UserRegistrationView(TitleMixin, SuccessMessageMixin, CreateView):
    model = Users
    template_name = 'user/register.html'
    form_class = UserRegisterForm
    success_url = reverse_lazy('user:login')
    success_message = 'Регистрация прошла успешно! Подтвердите адрес элекронной почты.'
    title = 'DeadStore|Регистрация'


class UserProfileView(TitleMixin, UpdateView):
    model = Users
    template_name = 'user/profile.html'
    form_class = UserRegisterForm
    title = 'Store - Профиль'

    def get_success_url(self):
        return reverse_lazy('user/profile.html', args=(self.object.id,))


class EmailVerificationView(TitleMixin, TemplateView):
    model = EmailVerification
    title = 'DeadStore - Подтверждение регистрации'
    template_name = 'user/email_verification.html'

    def get(self, request, *args, **kwargs):
        code = kwargs['code']
        user = Users.objects.get(email=kwargs['email'])
        email_verification = EmailVerification.objects.filter(user=user, code=code)
        if email_verification.exists() and not email_verification.first().is_expired():
            user.is_verified_mail = True
            user.save()
            return super(EmailVerificationView, self).get(self, request, *args, **kwargs)
        else:
            return HttpResponseRedirect(reverse('index'))
