from django.contrib import admin

from .models import Word


@admin.register(Word)
class WordAdmin(admin.ModelAdmin):
    """Admin for Word model"""

    fieldsets = (
        (None, {
            'fields': (('name', 'translation'), 'theme')
        }),
        ('Additional', {
            'classes': ('extrapretty',),
            'fields': (('transcription', 'plural', 'example'),)
        }),
        ('Media', {
            'classes': ('collapse',),
            'fields': (('picture_preview', 'picture'),
                       ('sound_preview', 'sound'))
        }),
    )
    list_display = (
        'id',
        'name',
        'translation',
        'theme',
    )
    list_display_links = (
        'id',
        'name',
        'translation',
    )
    list_filter = (
        'theme__level',
    )
    autocomplete_fields = (
        'theme',
    )
    search_fields = (
        'name',
        'translation',
        'example',
    )
    ordering = (
        'theme__level',
        'name'
    )
    readonly_fields = (
        'picture_preview',
        'sound_preview'
    )
