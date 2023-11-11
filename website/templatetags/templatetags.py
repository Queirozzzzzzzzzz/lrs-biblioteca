from django import template

register = template.Library()

@register.filter

def unescape(value):
    return value.replace('\\', '')
