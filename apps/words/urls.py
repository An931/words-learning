from . import views
from rest_framework.routers import DefaultRouter
from django.urls import path, include

router = DefaultRouter()
# router.register('', views.WordList.as_view(), basename='words-list')
router.register('', views.WordViewSet, basename='words-list')
# not work, try url. todo add query to router mb

# urlpatterns = (
#     path('', views.WordList.as_view()),
# )
