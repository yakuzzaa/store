from django.contrib.auth.forms import AuthenticationForm
from user.models import Users


class UserLoginForm(AuthenticationForm):
    class Meta:
        model = Users
        fields = ('username', 'password ')
