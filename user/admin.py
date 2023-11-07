from django.contrib import admin
from products.admin import BasketAdmin
from user.models import Users


@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    list_display = ('username',)
    inlines = (BasketAdmin,)
