from django.db.models import Count
from rest_framework.generics import ListAPIView

from main.models import Tag, Cocktail
from main.serializers.cocktail import CocktailSerializer


class CocktailWithTagAndMinIngredientsView(ListAPIView):
    serializer_class = CocktailSerializer

    def get_queryset(self):
        tag_name = self.kwargs["tag"]
        min_ingredients = int(self.kwargs["min"])
        tag = Tag.objects.get(name=tag_name)
        cocktails = Cocktail.objects.annotate(
            ingredient_count=Count("ingredients")
        ).filter(ingredient_count__gte=min_ingredients, tags=tag)
        return cocktails
