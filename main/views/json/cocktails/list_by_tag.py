from rest_framework.generics import ListAPIView

from main.models import Tag, Cocktail
from main.serializers.cocktail import CocktailSerializer


class CocktailsByTagView(ListAPIView):
    serializer_class = CocktailSerializer

    def get_queryset(self):
        tag_name = self.kwargs["tag"]
        tag = Tag.objects.get(name=tag_name)
        return Cocktail.objects.filter(tags=tag)
