from django import template
from django.utils.safestring import mark_safe



register = template.Library()

@register.filter(name='transform')
def transform(value):

    pseudoTags = [
        "*", "!",
        "%", ";",
        "&", "-)",
        "@", "|", "$"
        ]
    htmlTags = [
        "<b>", "</b>",
        "<i>", "</i>",
        "<figure class='img-post-1'><img class='img-t' src='", "' /></figure>",
        "<a href='", "' target='_blank' class='link'>", "</a>"
        ]
    for cont in range(0, len(pseudoTags)):
        if pseudoTags[cont] in value:
            value = value.replace(pseudoTags[cont], htmlTags[cont])

    return mark_safe(value)
   
