
from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display=['email','full_name','date_joined','last_login','is_active','is_admin']
    list_filter = ('is_admin','is_active','date_joined',)

