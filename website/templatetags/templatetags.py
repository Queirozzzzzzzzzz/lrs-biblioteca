from django import template

register = template.Library()

# Filtros

# Caractéres especiais
@register.filter
def unescape(value):
    return value.replace('\\', '')

# Número positivo
@register.filter(name='abs')
def abs_filter(value):
    return abs(value)
