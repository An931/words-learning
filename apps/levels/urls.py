from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', views.LevelViewSet, basename='levels-list')

