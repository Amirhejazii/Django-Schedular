from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin
from .forms import *

# Register your models here.

class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {
            'classes': ['wide'],
            'fields': ('is_superuser', 'is_staff', 'is_active', 'groups', 'permissions')
        }),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('first_name', 'last_name','email', 'password1', 'password2', 'is_staff', 'is_active','groups','username')}
        ),
    )
    model = User
    add_form = CustomUserCreationForm
    fieldsets = (
        *UserAdmin.fieldsets,
    )
    

admin.site.register(User,CustomUserAdmin)