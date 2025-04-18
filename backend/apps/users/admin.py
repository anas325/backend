from django.contrib import admin
from .models import User, Group, notification
from django.contrib.auth.admin import UserAdmin
# Register your models here.

class CustomUserAdmin(UserAdmin):
    model = User
    # Add your custom fields to fieldsets
    fieldsets = UserAdmin.fieldsets + (
        ('Additional Info', {
            'fields': ('bio', 'profile_picture',),
        }),
    )

    # Optional: show fields in admin "add user" form too
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Additional Info', {
            'fields': ('bio', 'profile_picture',),
        }),
    )

    # Optional: customize list display in admin user list
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'bio')

admin.site.register(User, CustomUserAdmin)



#admin.site.register(User, UserAdmin)
admin.site.register(Group)
admin.site.register(notification)