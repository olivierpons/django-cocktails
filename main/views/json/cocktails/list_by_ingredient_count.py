from django.db.models import Count
from rest_framework.generics import ListAPIView

from main.models import Cocktail
from main.serializers.cocktail import CocktailSerializer


class CocktailsByIngredientCountView(ListAPIView):
    serializer_class = CocktailSerializer

    def get_queryset(self):
        ingredient_count = int(self.kwargs["count"])
        cocktails = Cocktail.objects.annotate(
            ingredient_count=Count("ingredients")
        ).filter(ingredient_count=ingredient_count)
        return cocktails
