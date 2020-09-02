from rest_framework import serializers

from .models import Theme
# from apps.tags.api.serializers import TagSerializer todo


class ThemeSerializer(serializers.ModelSerializer):
    # todo query params ??

    class Meta:
        model = Theme
        fields = (
            'id',
            'category',
            'level'
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