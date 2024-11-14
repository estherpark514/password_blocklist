from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    list_display = ('email', 'raw_password', 'encrypted_password', 'is_staff', 'is_active')
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('raw_password', 'encrypted_password')}),
    )
    readonly_fields = ('encrypted_password', 'raw_password')
    ordering = ('email',)

admin.site.register(CustomUser, CustomUserAdmin)
