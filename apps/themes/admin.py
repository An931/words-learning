from django.contrib import admin

from .models import Theme


@admin.register(Theme)
class ThemeAdmin(admin.ModelAdmin):

    # fields = ('name',)
    # todo


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
        'name',
    )
    list_filter = (
        'category',
        'level',
    )
