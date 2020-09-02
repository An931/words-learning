from . import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'', views.ThemeViewSet)
# router.register(r'', views.ThemeViewSet)

# urlpatterns = router.urls

