from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from permissions.api_key_permissions import APIKeyPermission
from .models import Level
from .serializers import LevelSerializer


class LevelViewSet(viewsets.ReadOnlyModelViewSet):
    """API view set for Level model"""

    queryset = Level.objects.all()
    serializer_class = LevelSerializer
    permission_classes = [APIKeyPermission | IsAuthenticated]
