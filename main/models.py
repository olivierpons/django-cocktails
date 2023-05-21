from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext as _
from datetime import datetime


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="%(class)s_created_by_users",
    )
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="%(class)s_updated_by_users",
    )

    class Meta:
        abstract = True

    @staticmethod
    def get_time_difference(date1, date2):
        """
        Calcule la différence entre deux dates et renvoie le résultat
        sous la forme 'x days x h x m x s'.
        """
        diff = date2 - date1
        days, seconds = diff.days, diff.seconds
        hours = seconds // 3600
        minutes = (seconds % 3600) // 60
        seconds = (seconds % 60)

        # Créer une liste vide pour stocker les parties du résultat
        result = []

        # Si les jours, les heures, les minutes ou les secondes ne sont pas
        # zéro, les ajouter à la liste du résultat :
        if days > 0:
            result.append(_("{} days").format(days))
        if hours > 0:
            result.append(_("{} h").format(hours))
        if minutes > 0:
            result.append(_("{} m").format(minutes))
        if seconds > 0:
            result.append(_("{} s").format(seconds))

        # Rejoindre les parties du résultat en une seule chaîne et la renvoyer
        if len(result) > 1:
            last = result.pop()
            return " and ".join([", ".join(result), last])
        elif result:
            return result[0]
        else:
            return "0 s"

    def get_relative_from_now(self, date):
        """
        Calcule la différence entre la date donnée et l'heure actuelle.
        """
        now = datetime.now()
        return self.get_time_difference(date, now)


def _path(instance, filename):
    return '{}/{}'.format(timezone.now().strftime('%Y-%m-%d'), filename)


class Image(TimeStampedModel):
    file = models.ImageField(upload_to=_path, default=None, null=True, blank=True)
    title = models.CharField(max_length=200, default=None, null=True, blank=True)

    def __str__(self):
        return self.title


class Tag(TimeStampedModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name or _("? no name ?")


class Quantity(TimeStampedModel):
    class Meta:
        verbose_name_plural = _("Quantities")

    class QuantityType(models.IntegerChoices):
        QTY_FLOAT = 1, _("float")
        QTY_EITHER = 2, _("either")
        QTY_INTERVAL = 3, _("interval")
        QTY_NOT_MEASURABLE = 4, _("not measurable")

    quantity_type = models.IntegerField(
        choices=QuantityType.choices, default=QuantityType.QTY_NOT_MEASURABLE
    )
    value = models.FloatField(null=True, blank=True, default=None)
    min_value = models.FloatField(null=True, blank=True, default=None)
    max_value = models.FloatField(null=True, blank=True, default=None)
    step = models.FloatField(null=True, blank=True, default=None)

    def __str__(self):
        if self.quantity_type == self.QuantityType.QTY_FLOAT:
            return f"{self.value}"
        if self.quantity_type == self.QuantityType.QTY_EITHER:
            return _("{} or {}").format(self.min_value, self.max_value)
        if self.quantity_type == self.QuantityType.QTY_INTERVAL:
            return _("between {} and {}").format(self.min_value, self.max_value)
        return _("not measurable")


class Ingredient(TimeStampedModel):
    name_singular = models.CharField(
        max_length=100, null=True, blank=True, default=None
    )
    name_plural = models.CharField(
        max_length=100, null=True, blank=True, default=None
    )
    images = models.ManyToManyField(Image, blank=True)

    def __str__(self):
        return self.name_singular or _("? no name singular ?")


class Unit(TimeStampedModel):
    name_singular = models.CharField(
        max_length=100, null=True, blank=True, default=None
    )
    name_plural = models.CharField(
        max_length=100, null=True, blank=True, default=None
    )

    def __str__(self):
        return self.name_singular or _("? no name singular ?")


class Cocktail(TimeStampedModel):
    title = models.CharField(max_length=200)
    summary = models.TextField()
    description = models.TextField()
    tags = models.ManyToManyField(Tag)
    images = models.ManyToManyField(Image, blank=True)

    def __str__(self):
        return self.title or _("? no title ?")


class CocktailIngredient(TimeStampedModel):
    cocktail = models.ForeignKey(
        Cocktail, on_delete=models.CASCADE, related_name='ingredients'
    )
    ingredient = models.ForeignKey(
        Ingredient, on_delete=models.CASCADE, default=None
    )
    quantity = models.ForeignKey(
        Quantity, on_delete=models.CASCADE, default=None
    )
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return f"{self.quantity} {self.unit} {self.ingredient}"
