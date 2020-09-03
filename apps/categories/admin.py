from django.contrib import admin

from .models import Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Admin for Category model"""

    fields = (
        'name',
        'translation',
        ('icon_preview', 'icon')
    )

    list_display = (
        'id',
        'name',
        'icon',
    )
    list_display_links = (
        'id',
        'name',
    )
    search_fields = (
        'name',
    )
    readonly_fields = (
        'icon_preview',
    )
#     todo add themes mb
# todo add img preview to admin only
