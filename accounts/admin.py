from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import User

class CustomUserAdmin(UserAdmin):
    pass

admin.site.register(User, CustomUserAdmin)
