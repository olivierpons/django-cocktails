from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from main.views.cocktails.create import CocktailCreateView
from main.views.cocktails.list_with_2_ingredients import CocktailWith2IngredientsListView
from main.views.cocktails.update import CocktailUpdateView
from main.views.index import IndexView
from main.views.json.cocktails.ingredient_count import CocktailIngredientCountView
from main.views.json.cocktails.list_by_ingredient import CocktailListByIngredientView
from main.views.json.cocktails.list_by_ingredient_count import CocktailsByIngredientCountView
from main.views.json.cocktails.list_by_tag import CocktailsByTagView
from main.views.json.cocktails.list_by_title import CocktailListByTitleView
from main.views.json.cocktails.list_with_tag_and_min_ingredients import CocktailWithTagAndMinIngredientsView
from main.views.json.cocktails.view_set import CocktailViewSet

router = DefaultRouter()
router.register(r"cocktails", CocktailViewSet)

urlpatterns = [
    path('__debug__/', include('debug_toolbar.urls')),

    # region "urls"
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
        "cocktails/create", CocktailCreateView.as_view(), name="cocktail_create"
    ),
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

    path(
        "cocktail-with-2-ingredients/<str:ing1>/<str:ing2>",
            CocktailWith2IngredientsListView.as_view(),
        name="cocktail-with-2-ingredients",
    ),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
