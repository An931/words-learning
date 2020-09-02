from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'levels', views.LevelViewSet)

