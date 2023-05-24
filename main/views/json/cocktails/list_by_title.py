from rest_framework.generics import ListAPIView

from main.models import Cocktail
from main.serializers.cocktail import CocktailSerializer


class CocktailListByTitleView(ListAPIView):
    serializer_class = CocktailSerializer

    def get_queryset(self):
        title = self.kwargs["title"]
        return Cocktail.objects.filter(title__icontains=title)
