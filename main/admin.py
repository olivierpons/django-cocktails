from django.contrib import admin

from main.models import (
    Image,
    Tag,
    Ingredient,
    Unit,
    Cocktail,
    CocktailIngredient,
    Quantity,
)


class CocktailIngredientInlineAdmin(admin.TabularInline):
    model = CocktailIngredient
    extra = 0


class CocktailAdmin(admin.ModelAdmin):
    search_fields = ("title",)
    fields = ("title",)
    inlines = (CocktailIngredientInlineAdmin,)
    list_per_page = 500


admin.site.register(Image)
admin.site.register(Tag)
admin.site.register(Ingredient)
admin.site.register(Unit)
admin.site.register(Quantity)
admin.site.register(Cocktail, CocktailAdmin)
admin.site.register(CocktailIngredient)
