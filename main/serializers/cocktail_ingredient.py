from rest_framework import serializers
from main.models import CocktailIngredient, Ingredient, Quantity, Unit


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ['name_singular', 'name_plural']


class QuantitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Quantity
        fields = ['quantity_type', 'value', 'min_value', 'max_value', 'step']


class UnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unit
        fields = ['name_singular', 'name_plural']


class CocktailIngredientSerializer(serializers.ModelSerializer):
    ingredient = IngredientSerializer(read_only=True)
    quantity = QuantitySerializer(read_only=True)
    unit = UnitSerializer(read_only=True)

    class Meta:
        model = Ingredient
        fields = ['ingredient', 'quantity', 'unit']
