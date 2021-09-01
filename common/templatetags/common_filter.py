import markdown
from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter(name='omit')
def omit(value):
    value = str(value)
    return value if len(value) <= 10 else value[:10] + '...'
