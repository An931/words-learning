from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', views.CategoryViewSet, basename='categories-list')

# urlpatterns = router.urls  # todo or not