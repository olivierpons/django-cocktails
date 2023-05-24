from django.db.models import Q
from django.views.generic import ListView

from main.models import Cocktail


class CocktailWith2IngredientsListView(ListView):
    template_name = "crudl/cocktail/list.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        result = super().get_context_data(**kwargs)

        ing1 = self.kwargs["ing1"]
        ing2 = self.kwargs["ing2"]
        result["title"] = "Liste des cocktails qui contiennent {} ou {}".format(
            ing1, ing2
        )
        return result

    def get_queryset(self):
        ing1 = self.kwargs["ing1"]
        ing2 = self.kwargs["ing2"]
        return (
            Cocktail.objects.prefetch_related("ingredients__ingredient")
            .prefetch_related("ingredients__quantity")
            .prefetch_related("ingredients__unit")
            .filter(
                Q(ingredients__ingredient__name_singular__icontains=ing1)
                | Q(ingredients__ingredient__name_plural__icontains=ing1)
            )
            .filter(
                Q(ingredients__ingredient__name_singular__icontains=ing2)
                | Q(ingredients__ingredient__name_plural__icontains=ing2)
            )
            .distinct()
        )
