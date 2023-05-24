from django import forms
from main.models import Cocktail, Image


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ("created_by", "updated_by", "title", "file")


class CocktailForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        if "request" in kwargs:
            self.request = kwargs.pop("request")
        else:
            self.request = None
        super().__init__(*args, **kwargs)

    image = forms.ImageField(required=False)
    image_title = forms.CharField(required=False)

    class Meta:
        model = Cocktail
        fields = ("title",)

    def save(self, commit=True):
        self.instance.created_by = self.request.user
        self.instance.updated_by = self.request.user
        return super().save(commit)
