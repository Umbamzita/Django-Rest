from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomerUser

class CustomUserAdmin(UserAdmin):
    model = CustomerUser


admin.site.register(CustomerUser, CustomUserAdmin)
