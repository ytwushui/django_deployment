from django import template

register = template.Library()

@register.filter(name='cutme')
# pass the following function to the register.filter and return to the name cutme
def cut(value, arg):
    """
    this cuts out all values of "arg" frim the sting~
    """

    return value.replace(arg,'')
"""
register.filter('cutme',cut)
use decorate to replce this
"""
#(p1, the sting you need to call the function, p2,the function itself)
