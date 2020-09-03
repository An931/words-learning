from rest_framework import generics, viewsets

from permissions.api_key_permissions import APIKeyPermission

from .models import Word
from .serializers import WordSerializer

# from rest_framework_api_key.permissions import HasAPIKey
from rest_framework.permissions import IsAuthenticated


class WordViewSet(viewsets.ModelViewSet):
    """API view set for Word model"""

    queryset = Word.objects.all()
    serializer_class = WordSerializer

    # todo check readonly and not
    permission_classes = [APIKeyPermission | IsAuthenticated]

    def get_queryset(self):
        # !!! todo add theme  param
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