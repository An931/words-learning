from rest_framework import serializers

from apps.categories.models import Category

# from apps.tags.api.serializers import TagSerializer
from .models import Word


class WordSerializer(serializers.ModelSerializer):
    """Simple serializer for Word model"""

    class Meta:
        model = Word
        fields = (
            'id',
            'name',
            'translation',
            'example',
            'picture',
            'sound',
            'theme',
        )
        read_only_fields = (
            'theme',
        )


class ShortWordSerializer(serializers.ModelSerializer):
    """Short serializer for Word model.
     fields:
      id
      name
      translation
    """

    class Meta:
        model = Word
        fields = (
            'id',
            'name',
            'translation',
        )

