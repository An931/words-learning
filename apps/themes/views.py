from rest_framework import viewsets
from .models import Theme
from .serializers import ThemeSerializer


class ThemeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Theme.objects.all()
    serializer_class = ThemeSerializer
