from django.db.models import Count
from rest_framework.response import Response
from rest_framework.views import APIView

from main.models import CocktailIngredient
from main.serializers.cocktail_ingredient_count import IngredientCountSerializer


class CocktailIngredientCountView(APIView):
    def get(self, request):
        data = (
            CocktailIngredient.objects.values("ingredient__name_singular")
            .annotate(count=Count("cocktail"))
            .order_by("-count")
        )
        serializer = IngredientCountSerializer(data, many=True)
        return Response(serializer.data)
