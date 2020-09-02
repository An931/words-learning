from rest_framework import serializers

from apps.categories.models import Category
# from apps.tags.api.serializers import TagSerializer
from .models import Word


class WordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Word
        fields = (
            'id',
            'name',
            'translation',
            'transcription',
            'example',
            'sound',
        )
        # todo id in url