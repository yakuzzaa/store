from django.urls import path
from django.contrib.auth.decorators import login_required
from user.views import UserRegistrationView, UserLoginView, EmailVerificationView, UserProfileView
from django.contrib.auth.views import LogoutView

app_name = 'user'
urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('email_verification/<str:email>/<uuid:code>/', EmailVerificationView.as_view(), name="email_verification"),
    path('profile/<int:pk>/', login_required(UserProfileView.as_view()), name='profile'),
    path('logout/', LogoutView.as_view(), name='logout')
]
