from django.shortcuts import render
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Category
from .serializers import CategorySerializer


class CategoryViewSet(viewsets.ModelViewSet):
    """API view set for Category model"""

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    # todo check posts and gets
    # todo validate date
    # todo del post and add in levels