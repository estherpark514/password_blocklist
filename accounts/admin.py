from django.contrib import admin
from .models import CustomUser

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'encrypted_password', 'is_staff', 'is_active')
    
    readonly_fields = ('encrypted_password',)

admin.site.register(CustomUser, CustomUserAdmin)
