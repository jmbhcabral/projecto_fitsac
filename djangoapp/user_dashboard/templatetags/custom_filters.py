from django import template
import os

register = template.Library()


@register.filter
def basename(value):
    ''' Get basename from path '''
    return os.path.basename(value)


@register.filter
def get_item(dictionary, key):
    ''' Get item from dictionary '''
    return dictionary.get(key, [])
