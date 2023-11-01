from django.urls import path

from user.views import register, login, email_verification, profile

app_name = 'user'
urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('email_verification/', email_verification, name="email_verification"),
    path('profile/', profile, name='profile'),
]
