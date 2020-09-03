"""words_learning URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
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

    # # path('api/categories', include('apps.categories.urls')),
    # path('api/categories', include(categories_router.urls)),
    # # path('api/themes', include(themes_router.urls)),
    # # path('api/', include(themes_router.urls)),
    # path('api/words', include(words_router.urls)),
    # # path('api/words', include('apps.words.urls')),
    #
    # path('api/levels', include(levels_router.urls)),
]
