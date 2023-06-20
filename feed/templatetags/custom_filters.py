from django import template

register = template.Library()

@register.filter(name="endswith")
def endswith(string:str, ending:str):

    if isinstance(string, str):
        return string.endswith(tuple(ending.split()))
    return False
