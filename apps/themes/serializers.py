from rest_framework import serializers

from .models import Theme

# from apps.tags.api.serializers import TagSerializer todo


class ThemeSerializer(serializers.ModelSerializer):
    """Serializer for Theme model including words list"""

    class Meta:
        model = Theme
        fields = (
            'id',
            'category',
            'level',
            'name',
            'photo',
            # 'words', todo
        )

# todo another serializer with id
# fields=(
#     'id',
#     'category',
#     'level'
#     'name',
#     'photo',
#     'words' -- how?
# )