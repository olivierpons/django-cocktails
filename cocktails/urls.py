from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from main.views import IndexView, CocktailViewSet, CocktailSearchView

router = DefaultRouter()
router.register(r'cocktails', CocktailViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('drf/', include(router.urls)),
    path('search/', CocktailSearchView.as_view(), name='cocktail_search'),
    path('', IndexView.as_view(), name='index')
]
