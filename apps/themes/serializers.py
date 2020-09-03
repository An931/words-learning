from rest_framework import serializers

from .models import Theme

# from apps.tags.api.serializers import TagSerializer todo
from apps.words.serializers import WordSerializer


class ThemeSerializer(serializers.ModelSerializer):
    """Serializer for Theme model including words list"""

    words_serializer = WordSerializer(many=True, read_only=True, source='words')

    class Meta:
        model = Theme
        fields = (
            'id',
            'category',
            'level',
            'name',
            'photo',
            # 'words', todo
            'words_serializer',
        )
        # depth=1
#         https://www.django-rest-framework.org/api-guide/serializers/#modelserializer
        readonly_fields=(
            'words_serializer',
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