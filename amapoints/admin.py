from django.contrib import admin
from .models import Amapoints

# Register your models here.
class Admin(admin.ModelAdmin):
    pass

admin.site.register(Amapoints, Admin)
