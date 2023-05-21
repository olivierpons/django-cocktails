from django.contrib.auth.models import User
from django.db import models
from django.db.models import (
    Count,
    Q,
    Sum,
    Avg,
    ExpressionWrapper,
    F,
    Variance,
    Case,
    When,
    Exists,
)
from django.db.models import FloatField
from django.db.models import Subquery, OuterRef, Window
from django.db.models import Value
from django.db.models.aggregates import Aggregate
from django.db.models.functions import Now, ExtractYear, TruncDate
from django.db.models.functions import (
    RowNumber,
    Cast,
    Lower,
    Upper,
    Length,
    Coalesce,
    Concat,
    Trunc,
)
from django.forms import IntegerField, DateField
from django.shortcuts import get_object_or_404
from django.utils.translation import gettext_lazy as _
from django.views.generic import TemplateView, UpdateView
from rest_framework import viewsets
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .forms import CocktailForm
from .models import Cocktail, CocktailIngredient
from .serializers.cocktail import CocktailSerializer


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        result = super().get_context_data(**kwargs)
        # Calculer le nombre total de cocktails et la moyenne des ingrédients par cocktail
        aggregated_data = Cocktail.objects.aggregate(
            total_cocktails=Count("id", distinct=True),
            avg_ingredients=Avg("ingredients__quantity__value"),
            total_ingredients=Sum("ingredients__quantity__value"),
        )
        result["total_cocktails"] = aggregated_data["total_cocktails"]
        result["total_ingredients"] = aggregated_data["total_ingredients"]
        result["avg_ingredients"] = aggregated_data["avg_ingredients"]

        # Q: Utilisé pour les recherches complexes.
        # This will return all cocktails that have titles containing either "rum" or "gin".
        # Cette requête renverra tous les cocktails dont les titres contiennent soit "rum", soit "gin".
        cocktails = Cocktail.objects.filter(
            Q(title__icontains="rum") | Q(title__icontains="gin")
        )

        # Prefetch: Optimise la récupération des objets associés.
        # This will get all cocktails and their related ingredients in a single database query.
        # Cela récupère tous les cocktails et leurs ingrédients associés en une seule requête à la base de données.
        cocktails = Cocktail.objects.all().prefetch_related("ingredients")

        # Subquery: Intègre une sous-requête dans un QuerySet.
        # This will annotate each user with the title of a cocktail they created.
        # Cela annotera chaque utilisateur avec le titre d'un cocktail qu'ils ont créé.
        subquery = Cocktail.objects.filter(created_by=OuterRef("pk")).values(
            "title"
        )
        users_with_cocktails = User.objects.annotate(
            cocktail_title=Subquery(subquery[:1])
        )

        # OuterRef: Utilisé conjointement avec une Subquery.
        # In this case, it's used to refer to the primary key of the User model.
        # Dans ce cas, il est utilisé pour faire référence à la clé primaire du modèle User.

        # Window: Fournit un moyen d'appliquer des fonctions de fenêtre dans les requêtes.
        # This example will number each cocktail created by a user.
        # Cet exemple numérote chaque cocktail créé par un utilisateur.
        window_expression = Window(
            expression=RowNumber(),
            partition_by=[F("created_by")],
            order_by=F("created_at").desc(),
        )

        cocktails = Cocktail.objects.annotate(row_number=window_expression)

        # RowNumber: Attribue un numéro de ligne unique à chaque enregistrement dans la requête.
        # Used in conjunction with Window.
        # Utilisé en conjonction avec Window.

        # Avg: Calcule la moyenne d'un champ donné sur tous les objets d'un QuerySet.
        # This will return the average quantity used in all cocktails.
        # Cela renverra la quantité moyenne utilisée dans tous les cocktails.
        average_quantity = CocktailIngredient.objects.aggregate(
            Avg("quantity__value")
        )

        # Min: Calcule le minimum d'un champ donné sur tous les objets d'un QuerySet.
        # This will return the cocktail with the least ingredients.
        # Cela renverra le cocktail avec le moins d'ingrédients.
        min_ingredients = (
            Cocktail.objects.annotate(num_ingredients=Count("ingredients"))
            .order_by("num_ingredients")
            .first()
        )

        # Max: Calcule le maximum d'un champ donné sur tous les objets d'un QuerySet.
        # This will return the cocktail with the most ingredients.
        # Cela renverra le cocktail avec le plus d'ingrédients.
        max_ingredients = (
            Cocktail.objects.annotate(num_ingredients=Count("ingredients"))
            .order_by("-num_ingredients")
            .first()
        )

        # Sum: Calcule la somme d'un champ donné sur tous les objets d'un QuerySet.
        # Calculates the sum of a given field across all objects in a QuerySet.
        # Cela renverra la quantité totale de tous les ingrédients utilisés dans tous les cocktails.
        # This will return the total quantity of all ingredients used in all cocktails.
        total_quantity = CocktailIngredient.objects.aggregate(
            Sum("quantity__value")
        )

        # Case: Permet l'utilisation d'expressions conditionnelles dans les requêtes.
        # When: pour créer la condition "plus de 5 ingrédients".
        # Value: Utilisé pour envelopper les valeurs dans les requêtes.
        # Allows conditional expressions to be used in queries.
        # Cela annotera chaque cocktail avec une chaîne indiquant s'il est
        # "populaire" (plus de 5 ingrédients).
        # This will annotate each cocktail with a string indicating if it's
        # "popular" (more than 5 ingredients).
        cocktails = Cocktail.objects.annotate(
            ingredients_count=Count("ingredients")
        ).annotate(
            popularity=Case(
                When(ingredients_count__gt=5, then=Value("Popular")),
                default=Value("Not popular"),
                output_field=models.CharField(),
            )
        )

        # Exists: Vérifie l'existence d'objets dans une sous-requête.
        # Checks for the existence of objects in a subquery.
        # Cela renverra True si l'utilisateur a créé des cocktails, et False sinon.
        # This will return True if the user has created any cocktails, and False otherwise.
        has_created_cocktails = Exists(
            Cocktail.objects.filter(created_by=self.request.user)
        )

        # ExpressionWrapper: Utilisé pour envelopper les expressions complexes.
        # Used to wrap complex expressions.
        # Dans cet exemple, il est utilisé pour calculer le carré de la valeur de la quantité.
        # In this example, it's used to compute the square of the quantity value.
        squared_quantity = CocktailIngredient.objects.annotate(
            squared_quantity=ExpressionWrapper(
                F("quantity__value") * F("quantity__value"),
                output_field=FloatField(),
            )
        )

        # Coalesce: Renvoie la première valeur non nulle.
        # Returns the first non-null value.
        # Cela renverra le nom singulier de l'unité si le nom pluriel est nul, et vice versa.
        # This will return the singular name of the unit if the plural name is null, and vice versa.
        unit_name = Coalesce("unit__singular_name", "unit__plural_name")

        # Concat: Concatène plusieurs champs ou valeurs.
        # Concatenates several fields or values.
        # Cela concaténera le prénom et le nom d'un utilisateur, séparés par un espace.
        # This will concatenate a user's first name and last name, separated by a space.
        full_name = Concat("first_name", Value(" "), "last_name")

        # Length: Calcule la longueur d'un champ CharField.
        # Calculates the length of a CharField.
        # Cela renverra la longueur du titre d'un cocktail.
        # This will return the length of a cocktail's title.
        title_length = Length("title")

        # Upper: Convertit un champ CharField en majuscules.
        # Converts a CharField to uppercase.
        # Cela renverra le titre d'un cocktail en majuscules.
        # This will return a cocktail's title in uppercase.
        upper_title = Upper("title")

        # Lower: Convertit un champ CharField en minuscules.
        # Converts a CharField to lowercase.
        # Cela renverra le titre d'un cocktail en minuscules.
        # This will return a cocktail's title in lowercase.
        lower_title = Lower("title")

        # Cast: Change le type de données d'un champ.
        # Changes the data type of a field.
        # Cela convertira la valeur de la quantité en IntegerField.
        # This will convert the quantity value to an IntegerField.
        integer_quantity = Cast("quantity__value", IntegerField())

        # Trunc: Tronque un champ DateTime à un type de données spécifique.
        # Truncates a DateTimeField to a specific data type.
        # Cela tronquera la date de création d'un cocktail à la date (sans heure).
        # This will truncate a cocktail's creation date to the date (without time).
        # Annotate each cocktail with its creation date (without time)
        cocktails = Cocktail.objects.annotate(
            creation_date=TruncDate('created_at')
        )

        # Now you can access 'creation_date' for each cocktail
        for cocktail in cocktails:
            print(f"{cocktail.title} was created on {cocktail.creation_date}.")

        # Annotate each cocktail with its creation year
        cocktails = Cocktail.objects.annotate(
            creation_year=ExtractYear('created_at')
        )

        # Now you can access 'creation_year' for each cocktail
        for cocktail in cocktails:
            print(f"{cocktail.title} was created in {cocktail.creation_year}.")

        # Expression to calculate the age of the cocktail in days
        age_expression = ExpressionWrapper(
            Now() - F('created_at'),
            output_field=models.DurationField()
        )

        # Annotate each cocktail with its age
        cocktails = Cocktail.objects.annotate(
            age=age_expression
        )

        # Now you can access 'age' for each cocktail
        for cocktail in cocktails:
            # The age is a timedelta object, to get the number of days you can use .days
            print(f"The cocktail {cocktail.title} is {cocktail.age.days} days old.")

        return result


class CocktailViewSet(viewsets.ModelViewSet):
    queryset = Cocktail.objects.all()
    serializer_class = CocktailSerializer


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


class CocktailListByTitleView(ListAPIView):
    serializer_class = CocktailSerializer

    def get_queryset(self):
        title = self.kwargs['title']
        return Cocktail.objects.filter(title__icontains=title)


class CocktailUpdateView(UpdateView):
    model = Cocktail
    form_class = CocktailForm
    template_name = 'cocktail_update.html'
    success_url = '/'

    def form_valid(self, form):
        form.instance.updated_by = self.request.user
        return super().form_valid(form)