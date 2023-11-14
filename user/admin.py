from django.contrib import admin
from products.admin import BasketAdmin
from user.models import Users, EmailVerification


@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    list_display = ('username',)
    inlines = (BasketAdmin,)


@admin.register(EmailVerification)
class EmailVerification(admin.ModelAdmin):
    list_display = ('code', 'user', 'expiration',)
    fields = ('code', 'user', 'expiration', 'created')
    readonly_fields = ('created',)
