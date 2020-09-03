
from django.contrib import admin
from django.contrib.auth.models import Group

from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """Admin for User model"""

    fields = (
        'email',
        'name',
        'is_superuser',
    )

    list_display = (
        'id',
        'email',
        'name',
        'date_joined',
        'last_login',
        'is_active',
        'is_staff',
        'is_superuser',
    )
    search_fields = (
        'name',
        'email',
    )
    list_display_links = ('id', 'email',)


# remove Group model from admin
admin.site.unregister(Group)
