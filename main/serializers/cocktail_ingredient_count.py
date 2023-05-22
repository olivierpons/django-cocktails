from rest_framework import serializers


class IngredientCountSerializer(serializers.Serializer):
    ingredient = serializers.CharField(source="ingredient__name_singular")
    count = serializers.IntegerField()


