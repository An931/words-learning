from rest_framework import serializers

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
    """Short serializer for Word model"""

    class Meta:
        model = Word
        fields = (
            'id',
            'name',
            'translation',
        )

