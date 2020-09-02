from django.contrib import admin

from .models import Level


@admin.register(Level)
class LevelAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'name',
        'code',
    )
    search_fields = (
        'name',
        'code',
    #     maybe del in autocomplete (but do with filter)
    )
    # list_filter = (
    #     # todo it will be in others
    #     'code',
    # )

    # def has_add_permission(self, request):
    #     return False
    #
    # def has_delete_permission(self, request, obj=None):
    #     return False
#     todo update too
