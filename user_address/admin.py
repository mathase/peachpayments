from django.contrib import admin
from .models import User_Address

# Register your models here.

class Admin(admin.ModelAdmin):
    pass

admin.site.register(User_Address, Admin)
