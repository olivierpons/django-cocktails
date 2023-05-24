from django.views.generic import UpdateView

from main.forms import CocktailForm, ImageForm
from main.models import Cocktail


class CocktailUpdateView(UpdateView):
    model = Cocktail
    template_name = "cocktail_update.html"
    success_url = "/drf/"

    def get_form(self, form_class=None):
        return CocktailForm(request=self.request)

    def form_invalid(self, form):
        return super().form_invalid(form)

    def form_valid(self, form):
        image_form = ImageForm(
            {
                "created_by": self.request.user,
                "updated_by": self.request.user,
                "title": self.request.POST.get("image_title"),
            },
            self.request.FILES,
        )

        if image_form.is_valid():
            image = image_form.save()
            self.object.images.add(image)

        return super().form_valid(form)
