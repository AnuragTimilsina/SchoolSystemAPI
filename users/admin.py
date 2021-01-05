from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group

from .models import User
# Register your models here.


class UserAdmin(BaseUserAdmin):
    add_fieldsets = ((None, {
        'fields': ('email', 'username', 'is_student', 'is_teacher', 'password', 'password2')
    }), ('Permissions', {
        'fields': ('is_superuser', 'is_staff')
    }))

    fieldsets = ((None, {
        'fields': ('email', 'username', 'is_student', 'is_teacher', 'password2')
    }), ('Permissions', {
        'fields': ('is_superuser', 'is_staff')
    }))

    list_display = ['email', 'username', 'is_student', 'is_teacher']
    search_fields = ('email', 'username')
    ordering = ('email', )


admin.site.register(User, UserAdmin)
admin.site.unregister(Group)