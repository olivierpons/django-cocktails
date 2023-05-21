from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from main.views import (
    IndexView,
    CocktailViewSet,
    CocktailListByIngredientView,
    CocktailListByTitleView,
    CocktailUpdateView,
)

router = DefaultRouter()
router.register(r"cocktails", CocktailViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
    path("drf/", include(router.urls)),
    path(
        "cocktails-by-ingredient/",
        CocktailListByIngredientView.as_view(),
        name="cocktail_search",
    ),
    path("cocktails-by-title/<str:title>/", CocktailListByTitleView.as_view()),
    path(
        "cocktail-update/<int:pk>/",
        CocktailUpdateView.as_view(),
        name="cocktail-update",
    ),
    path("", IndexView.as_view(), name="index"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
