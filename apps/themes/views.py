from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from permissions.api_key_permissions import APIKeyPermission

from .models import Theme
from .serializers import ThemeSerializer


class ThemeViewSet(viewsets.ModelViewSet):
    """API view set for Theme model"""

    queryset = Theme.objects.all()
    serializer_class = ThemeSerializer
    permission_classes = [APIKeyPermission | IsAuthenticated]

    def get_queryset(self):
        """Filter by query params category and level"""
        queryset = Theme.objects.all()

        category_id = self.request.query_params.get('category', None)
        if category_id:
            queryset = queryset.filter(category__id=category_id)

        level_id = self.request.query_params.get('level', None)
        if level_id:
            queryset = queryset.filter(level__id=level_id)
        return queryset
