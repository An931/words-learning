from django.contrib import admin

from .models import Level


@admin.register(Level)
class LevelAdmin(admin.ModelAdmin):
    """Admin for Level model"""

    list_display = (
        'id',
        'code',
        'name',
    )
    list_display_links = (
        'id',
        'code',
        'name',
    )
    search_fields = (
        'name',
        'code',
    )

    # def has_add_permission(self, request):
    #     return False
    #
    # def has_delete_permission(self, request, obj=None):
    #     return False
#     todo update too
# del action mb
