from core.models import User, Department
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin


class CustomUserAdmin(UserAdmin):

    ordering = ('email', )
    exclude = ('user_permissions', 'groups')
    search_fields = ('email', 'first_name', 'last_name')
    list_display = ('email', 'first_name', 'last_name')
    fieldsets = ()
    add_fieldsets = ()


class DepartmentAdmin(admin.ModelAdmin):

    list_display = ('name', 'is_active')

admin.site.register(User, CustomUserAdmin)
admin.site.register(Department, DepartmentAdmin)
