from django import template

register = template.Library()


@register.filter
def inc(a, b):
    a = int(a)
    b = int(b)
    return a + b


@register.simple_tag
def division(a, b, to_int=False):
    a = int(a)
    b = int(b)
    if to_int:
        return int(a / b)
    return a / b
