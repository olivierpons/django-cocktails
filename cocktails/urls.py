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
    CocktailsByIngredientCountView,
    CocktailsByTagView,
    CocktailWithTagAndMinIngredientsView,
    CocktailIngredientCountView,
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
    path(
        "cocktails-by-ingredient-count/<int:count>/",
        CocktailsByIngredientCountView.as_view(),
        name="cocktails-by-ingredient-count",
    ),
    path(
        "cocktails/tag/<str:tag>/",
        CocktailsByTagView.as_view(),
        name="cocktails-by-tag",
    ),
    path(
        "cocktails/tag/<str:tag>/ingredients/<int:min>/",
        CocktailWithTagAndMinIngredientsView.as_view(),
        name="complex-query",
    ),
    path(
        "cocktails/ingredient/count/",
        CocktailIngredientCountView.as_view(),
        name="ingredient-cocktail-count",
    ),
    # https://www.chartjs.org/docs/latest/samples/information.html
    # <!DOCTYPE html>
    # <html>
    # <body>
    # <canvas id="myChart"></canvas>
    # <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    # <script>
    # fetch('http://localhost:8000/cocktails/ingredient/count/')
    #     .then(response => response.json())
    #     .then(data => {
    #         const ctx = document.getElementById('myChart').getContext('2d');
    #         new Chart(ctx, {
    #             type: 'pie',
    #             data: {
    #                 labels: data.map(item => item.ingredient),
    #                 datasets: [{
    #                     data: data.map(item => item.count),
    #                     backgroundColor: [
    #                         '#ff6384', '#36a2eb', '#cc65fe', '#ffce56',
    #                         '#9b5de5', '#f15bb5', '#fee440', '#00bbf9',
    #                         '#7209b7', '#f71735'
    #                     ],  // a set of random colors
    #                 }],
    #             },
    #             options: {
    #                 responsive: true,
    #             }
    #         });
    #     });
    # </script>
    # </body>
    # </html>
    # """
    path("", IndexView.as_view(), name="index"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
