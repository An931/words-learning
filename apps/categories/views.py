from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from permissions.api_key_permissions import APIKeyPermission

from .models import Category
from .serializers import CategorySerializer


class CategoryViewSet(viewsets.ModelViewSet):
    """API view set for Category model"""

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [APIKeyPermission | IsAuthenticated]
