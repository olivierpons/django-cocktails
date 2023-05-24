from rest_framework import viewsets

from main.models import Cocktail
from main.serializers.cocktail import CocktailSerializer


class CocktailViewSet(viewsets.ModelViewSet):
    queryset = Cocktail.objects.all()
    serializer_class = CocktailSerializer
