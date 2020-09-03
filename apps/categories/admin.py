from django.contrib import admin
from django.utils.html import mark_safe

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

    def icon_preview(self, obj):
        """Preview for icon field"""
        return mark_safe(f'<img src="{obj.icon.url}" height="200"/>')
