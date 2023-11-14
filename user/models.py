from django.core.mail import send_mail
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from django.utils.timezone import now

from config.settings import DOMAIN_NAME


class Users(AbstractUser):
    image = models.ImageField(upload_to='users_images', null=True, blank=True)
    is_verified_mail = models.BooleanField(default=False)
    email = models.EmailField(unique=True, blank=False)


class EmailVerification(models.Model):
    code = models.UUIDField(unique=True)
    user = models.ForeignKey(to=Users, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    expiration = models.DateTimeField()

    def __str__(self):
        return f'EmailVeridication для {self.user.email}'

    def send_verification_email(self):
        link = reverse('user:email_verification', args=(self.user.email, self.code,))
        verification_link = f'{DOMAIN_NAME}{link}'
        subject = f'DeadStore|Подтверждение учетной записи пользователя {self.user.username}'
        message = f'Для подтверждения учетной записи перейдите по ссылке:{verification_link}'
        send_mail(
            subject=subject,
            message=message,
            from_email='DeadInsideStore@yandex.ru',
            recipient_list=[self.user.email],
            fail_silently=False
        )

    def is_expired(self):
        return True if now() >= self.expiration else False
