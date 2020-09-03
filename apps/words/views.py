from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from permissions.api_key_permissions import APIKeyPermission

from .models import Word
from .serializers import WordSerializer


class WordViewSet(viewsets.ModelViewSet):
    """API view set for Word model"""

    queryset = Word.objects.all()
    serializer_class = WordSerializer
    permission_classes = [APIKeyPermission | IsAuthenticated]

    def get_queryset(self):
        """Filter by theme"""
        queryset = Word.objects.all()
        theme_id = self.request.query_params.get('theme', None)
        if theme_id:
            queryset = queryset.filter(theme__id=theme_id)
        return queryset
