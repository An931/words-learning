from django.contrib import admin

from .models import Theme


@admin.register(Theme)
class ThemeAdmin(admin.ModelAdmin):
    """Admin for Theme model"""

    fields = (
        ('name', 'translation'),
        'category',
        'level',
        ('photo_preview', 'photo')
    )

    list_display = (
        'id',
        'name',
        'level',
        'category',
    )
    list_display_links = (
        'id',
        'name',
    )
    autocomplete_fields = (
        'category',
        'level',
    )
    search_fields = (
        'name',
        'translation'
    )
    ordering = (
        'level__code',
        'name',
    )
    list_filter = (
        'category',
        'level',
    )
    readonly_fields = ('photo_preview',)
