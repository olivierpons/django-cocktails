from django import forms
from main.models import Cocktail, Image


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ("created_by", "updated_by", "title", "file")


class CocktailForm(forms.ModelForm):
    image = forms.ImageField(required=False)
    image_title = forms.CharField(required=False)

    class Meta:
        model = Cocktail
        fields = ('title', )
