from django import template

register = template.Library()

def create_range(value, start_index=0):
    print("olo")
    return range(start_index, value+start_index)
	
def lower(value): # Only one argument.
    """Converts a string into all lowercase"""
    return value.lower()
	
def mod(value, arg):
    return value % arg
	
register.filter('create_range', create_range)
register.filter('lower', lower)
register.filter('mod', mod)