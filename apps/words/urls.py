from . import views
from rest_framework.routers import DefaultRouter
from django.urls import path, include

router = DefaultRouter()
router.register(r'', views.WordViewSet)

# not work, try url. todo add query to router mb

urlpatterns = router.urls

# urlpatterns = (
#     path('', views.WordList.as_view()),
# )
