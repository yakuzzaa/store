import uuid
from datetime import timedelta
from django.utils.timezone import now
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from user.models import Users, EmailVerification
from django import forms


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control py-4", "placeholder": "Введите имя пользователя"
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        "class": "form-control py-4", "placeholder": "Введите пароль"
    }))

    class Meta:
        model = Users
        fields = ('username', 'password ')


class UserRegisterForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control py-4", "placeholder": "Введите имя"
    }))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control py-4", "placeholder": "Введите фамилию"
    }))
    username = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control py-4", "placeholder": "Введите имя пользователя"
    }))
    email = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control py-4", "placeholder": "Введите адрес эл. почты"
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        "class": "form-control py-4", "placeholder": "Введите пароль"
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        "class": "form-control py-4", "placeholder": "Подтвердите пароль"
    }))

    class Meta:
        model = Users
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super(UserRegisterForm, self).save(commit=True)
        expiration = now() + timedelta(days=1)
        record = EmailVerification.objects.create(code=uuid.uuid4(), user=user, expiration=expiration)
        record.send_verification_email()
        return user



class UserProfileForm(UserChangeForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control py-4"
    }))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control py-4"
    }))
    image = forms.ImageField(widget=forms.FileInput(attrs={
        "class": "custom-file-input"
    }))
    username = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control py-4", "readonly": True
    }))
    email = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control py-4", "readonly": True
    }))

    class Meta:
        model = Users
        fields = ('first_name', 'last_name', 'image', 'username', 'email')
