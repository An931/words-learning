from rest_framework import serializers

from apps.words.models import Word
from apps.words.serializers import ShortWordSerializer

from .models import Theme


class ThemeSerializer(serializers.ModelSerializer):
    """Serializer for Theme model including words list"""

    words = serializers.SerializerMethodField('get_words')

    def get_words(self, theme):
        """Return serialized words set"""
        queryset = Word.objects.filter(theme=theme)
        serializer = ShortWordSerializer(many=True, instance=queryset)
        return serializer.data

    class Meta:
        model = Theme
        fields = (
            'id',
            'category',
            'level',
            'name',
            'photo',
            'words',
        )
