from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import CustomUser, Follow


class CustomUserAdmin(BaseUserAdmin):

    model = CustomUser
    fieldsets = BaseUserAdmin.fieldsets + (
        (None, {'fields': ('bio', 'location', 'website', 'profilepicture')}),
    )

# admin.site.register(CustomUser, CustomUserAdmin)
# admin.site.register(Follow)
