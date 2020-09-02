from rest_framework import viewsets
from .models import Word
from .serializers import WordSerializer
from rest_framework import generics


# class WordViewSet(viewsets.ReadOnlyModelViewSet):
#     # todo not readonly, check others
#     queryset = Word.objects.all()
#     serializer_class = WordSerializer

class WordList(generics.ListAPIView):
    # queryset = Word.objects.all()
    serializer_class = WordSerializer

    def get_queryset(self):
        # !!! todo query par need to be in themes!!!
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = Word.objects.all()
        name = self.request.query_params.get('name', None)
        if name:
            queryset = queryset.filter(name=name)
        # category_id = self.request.query_params.get('category', None)
        # if category_id:
        #     queryset = queryset.filter(category__id=category_id)
        #
        # level_id = self.request.query_params.get('level', None)
        # # todo what is none
        # if level_id:
        #     queryset = queryset.filter(level__id=level_id)

        return queryset