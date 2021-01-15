from django import template

register = template.Library()

@register.filter
def spliter(value, key):
  """
    Returns the value turned into a list.
  """
  return value.split(key)

register.filter('spliter', spliter)

@register.filter
def last_element(value, key):
  """
    Returns the value turned into a list.
  """
  split_data = value.split(key)
  return split_data[-1]

register.filter('last_element', last_element)