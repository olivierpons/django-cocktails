from django import template

register = template.Library()


@register.filter('klass')
def klass(field):
    """
    Renvoie le nom de la classe du widget qui doit être rendu
    http://stackoverflow.com/questions/
    1809874/get-type-of-django-form-widget-from-within-template

    Ici, modification de leur exemple :
    - j'essaie de récupérer le sous-champ "field"
    - et normalement dans ce sous-champ il doit y avoir "widget"
    -> dans tous les cas, si on ne trouve pas, ça renvoie la "base" = field
    -> dans tous les cas, on renverra un nom de classe même si ça n'est pas une
       classe de type widget
    Args:
        field:
    """
    if hasattr(field, 'getattr'):
        f = field.getattr('field', field)
        f = field.getattr('widget', f)
    else:
        f = field
    return f.__class__.__name__

