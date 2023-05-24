from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views.generic import CreateView

from main.forms import CocktailForm


class CocktailCreateView(LoginRequiredMixin, CreateView):
    form_class = CocktailForm

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({"request": self.request})
        return kwargs

    def get_success_url(self):
        messages.add_message(
            self.request, messages.INFO, message="Cocktail créé !"
        )
        return reverse("index")

    template_name = "crudl/cocktail/create.html"
