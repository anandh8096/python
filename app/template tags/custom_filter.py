from django import template


register = template.Library()


def small(value): # Only one argument.
    """Converts a string into all lowercase"""
    return value.upper()

    
register.filter('upper', small)
