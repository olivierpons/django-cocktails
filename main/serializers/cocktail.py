from rest_framework import serializers

from main.models import Cocktail
from main.serializers.cocktail_ingredient import CocktailIngredientSerializer
from main.serializers.tag import TagSerializer


class CocktailSerializer(serializers.ModelSerializer):
    ingredients = serializers.SerializerMethodField()

    @staticmethod
    def get_ingredients(obj):
        return CocktailIngredientSerializer(
            obj.ingredients.all(), many=True
        ).data

    tags = TagSerializer(many=True)

    class Meta:
        model = Cocktail
        fields = [
            'pk', 'title', 'summary', 'tags', 'ingredients',
        ]
        depth = 1
