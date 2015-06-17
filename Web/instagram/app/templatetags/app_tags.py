from django import template

register = template.Library()

@register.filter(name='getrelatedobjects')
def getrelatedojects(value):
    return value.all()

@register.filter(name='reverse_list')
def reverse_list(value):
    return reversed(value)
