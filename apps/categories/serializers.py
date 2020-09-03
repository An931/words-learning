from rest_framework import serializers

from apps.categories.models import Category


class CategorySerializer(serializers.ModelSerializer):
    """Simple serializer for Category model"""

    class Meta:
        model = Category
        fields = (
            'id',
            'name',
            'icon',
        )
