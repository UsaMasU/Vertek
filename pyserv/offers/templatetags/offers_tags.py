from django import template

register = template.Library()


@register.simple_tag()
def offer_tag():
    return 'Hello from offer_tag'
