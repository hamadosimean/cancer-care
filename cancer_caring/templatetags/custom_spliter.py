from django import template


register = template.Library()


@register.filter(name="spliter")
def spliter(value, index=2):
    """spliting string"""
    value = str(value)
    return value[:index]
