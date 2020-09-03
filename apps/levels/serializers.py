from rest_framework import serializers

from apps.levels.models import Level


class LevelSerializer(serializers.ModelSerializer):
    """Simple serializer for Level model"""

    class Meta:
        model = Level
        fields = (
            'id',
            'name',
            'code',
        )
