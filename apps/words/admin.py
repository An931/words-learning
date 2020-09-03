from django.contrib import admin

from .models import Word


@admin.register(Word)
class WordAdmin(admin.ModelAdmin):
    """Admin for Word model"""

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
    # add fieldsets
    list_filter = (
        'theme',
        'theme__level'
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
        'theme',
        'name'
        #     todo check
    )
    readonly_fields = ('picture_preview',
                       'sound_preview')
#     change order todo + add field sets
# https://docs.djangoproject.com/en/3.1/ref/contrib/admin/
