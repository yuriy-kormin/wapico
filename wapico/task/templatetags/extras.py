import json

from django import template

register = template.Library()


@register.filter
def pretty_json(value):
    return json.dumps(value, indent=4)


@register.filter
def is_list(value):
    return isinstance(value, list)
