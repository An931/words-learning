from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', views.WordViewSet, basename='words-list')
