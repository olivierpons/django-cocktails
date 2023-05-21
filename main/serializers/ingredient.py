from rest_framework import serializers

from main.models import Ingredient


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ['name_singular', 'name_plural']
