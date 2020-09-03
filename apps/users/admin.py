from django.contrib import admin

from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """Admin for User model"""

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

    # add_fieldsets = (
    #     (None, {
    #         'classes': ('wide',),
    #         'fields': ('email', 'password1', 'password2',),
    #     }),
    #     (_('Personal info'), {
    #         'fields': (
    #             'first_name',
    #             'last_name',
    #             'role',
    #             'phone_number',
    #         )
    #     })
    #
    # )
    # fieldsets = (
    #     (None, {'fields': ('email', 'password',)}),
    #     (_('Personal info'), {
    #         'fields': (
    #             'first_name',
    #             'last_name',
    #             'role',
    #             'phone_number',
    #         )
    #     }),
    #     (_('Permissions'), {
    #         'classes': (
    #             'collapse',
    #         ),
    #         'fields': (
    #             'is_active',
    #             'is_staff',
    #             'is_superuser',
    #             'groups',
    #             'user_permissions',
    #         )
    #     }),
    #     (_('Important dates'), {
    #         'fields': ('last_login', 'date_joined',)
    #     }),
    # )
    # readonly_fields = DjangoUserAdmin.readonly_fields + (
    #     'last_login',
    #     'date_joined',
    # )
    # list_filter = (
    #     'role',
    #     'is_active',
    #     'is_staff',
    #     'is_superuser',
    # )
    # ordering = ('email',)
    # actions = [deactivate]
    # change_actions = ['deactivate']