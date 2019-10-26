# Creating our own filters
from django import templates

register = template.Library()

@register.filter(name = 'cut')

def cut(value, arg):
    """
    This cuts out all values of 'args' from the string!
    """

    return value.replace(arg, '')

#register.filter('cut', cut)
# the above line contains first what you want to call it and then the name given to in this files
