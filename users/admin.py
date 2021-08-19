from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin
from django.forms import TextInput, Textarea


class UserAdminConfig(UserAdmin):
    model = User
    search_fields = ('email', 'user_id',)
    list_filter = ('email', 'user_id', 'is_active', 'is_staff')
    ordering = ('-date_joined',)
    list_display = ('email', 'user_id', 'date_joined',
                    'is_active', 'is_staff')
    fieldsets = (
        (None, {'fields': ('email', 'user_id', 'date_joined',)}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'user_id', 'password1', 'password2', 'is_active', 'is_staff')}
         ),
    )


admin.site.register(User, UserAdminConfig)
