from django.contrib import admin
from .models import Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    # todo check what else write

    list_display = [
        'id',
        'name',
        'icon',
    ]
    list_display_links = [
        'id',
        'name',
    ]
    search_fields = [
        'name',
    ]
