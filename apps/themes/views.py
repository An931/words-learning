from rest_framework import viewsets

from .models import Theme
from .serializers import ThemeSerializer


class ThemeViewSet(viewsets.ModelViewSet):
    """API view set for Theme model"""

    queryset = Theme.objects.all()
    serializer_class = ThemeSerializer

    def get_queryset(self):
        queryset = Theme.objects.all()

        category_id = self.request.query_params.get('category', None)
        if category_id:
            queryset = queryset.filter(category__id=category_id)

        level_id = self.request.query_params.get('level', None)
        # todo what is none
        if level_id:
            queryset = queryset.filter(level__id=level_id)
        return queryset
