from django.contrib import admin
from django.urls import include, path

from apps.categories.urls import router as categories_router
from apps.levels.urls import router as levels_router
from apps.themes.urls import router as themes_router
from apps.words.urls import router as words_router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/levels/', include(levels_router.urls)),
    path('api/categories/', include(categories_router.urls)),
    path('api/themes/', include(themes_router.urls)),
    path('api/words/', include(words_router.urls)),
]
