from django.db.models import Q
from rest_framework.response import Response
from rest_framework.views import APIView

from main.models import Cocktail, CocktailIngredient
from main.serializers.cocktail import CocktailSerializer
from django.utils.translation import gettext_lazy as _


class CocktailListByIngredientView(APIView):
    @staticmethod
    def get(request):
        ingredient_part = request.query_params.get("ingredient", None)
        if ingredient_part:
            serializer = CocktailSerializer(
                Cocktail.objects.filter(
                    id__in=CocktailIngredient.objects.filter(
                        Q(ingredient__name_singular__contains=ingredient_part)
                        | Q(ingredient__name_plural__contains=ingredient_part)
                    ).values("cocktail")
                ),
                many=True,
            )
            return Response(serializer.data)
        else:
            return Response(
                {"message": _("Please provide an ingredient name.")}
            )
