from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from calori.models import User, Item, ItemConsumption


@admin.register(User)
class AuthUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('username', 'first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser',
                                    'user_type', )}),
        ('Important dates', {'fields': ('last_login', 'date_joined')})
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'user_type'),
        }),
    )
    list_display = ('username', 'user_type', 'date_joined')
    list_filter = ('user_type', 'is_active')
    ordering = ('email', )
    search_fields = ("email",)

admin.site.register(Item)
admin.site.register(ItemConsumption)