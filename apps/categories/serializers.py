from rest_framework import serializers

from apps.categories.models import Category
# from apps.tags.api.serializers import TagSerializer


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = (
            'id',
            'name',
            'icon',
        )
#         todo what else
