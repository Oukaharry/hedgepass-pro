from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, AccountPair, PerformanceData

class CustomUserAdmin(UserAdmin):
    list_display = ('email', 'is_staff')
    search_fields = ('email',)
    ordering = ('email',)
    
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
    )

admin.site.register(User, CustomUserAdmin)
admin.site.register(AccountPair)
admin.site.register(PerformanceData)