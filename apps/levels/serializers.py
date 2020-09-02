from rest_framework import serializers

from apps.levels.models import Level


class LevelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Level
        fields = (
            'id',
            'name',
            'code',
        )
