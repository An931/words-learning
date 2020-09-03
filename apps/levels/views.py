from rest_framework import viewsets

from .models import Level
from .serializers import LevelSerializer


class LevelViewSet(viewsets.ReadOnlyModelViewSet):
    """API view set for Level model"""

    queryset = Level.objects.all()
    serializer_class = LevelSerializer
    permission_classes = '' #todo
