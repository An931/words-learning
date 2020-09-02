from django.contrib import admin
from .models import Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'icon',)
    list_display_links = ('id', 'name',)
    search_fields = ('name',)

    readonly_fields = ('icon_preview',)

