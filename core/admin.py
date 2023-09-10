from core.models import User, Department
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group


class CustomUserAdmin(UserAdmin):

    ordering = ('email', )
    exclude = ('user_permissions', 'groups')
    search_fields = ('email', 'first_name', 'last_name')
    list_display = ('email', 'is_active', 'first_name', 'last_name', 'department')
    list_filter = ('is_active', 'department')
    list_editable = ('is_active', )
    fieldsets = ()
    add_fieldsets = ()


class DepartmentAdmin(admin.ModelAdmin):

    list_display = ('name', 'is_active')

admin.site.unregister(Group)
admin.site.register(User, CustomUserAdmin)
admin.site.register(Department, DepartmentAdmin)

