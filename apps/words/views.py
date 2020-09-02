from rest_framework import viewsets
from .models import Word
from .serializers import WordSerializer


class WordViewSet(viewsets.ReadOnlyModelViewSet):
    # todo not readonly, check others
    queryset = Word.objects.all()
    serializer_class = WordSerializer
