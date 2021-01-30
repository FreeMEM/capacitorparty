import re
from django import template
from django.urls import reverse, NoReverseMatch

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


@register.simple_tag(takes_context=True)
def active(context, pattern_or_urlname):

    try:
        pattern = '^' + reverse(pattern_or_urlname)
    except NoReverseMatch:
        pattern = pattern_or_urlname
    path = context['request'].path
    # pattern = pattern_or_urlname
    # path = context['request'].path
    print("pattern: %s path %s - %s" % (pattern, path, re.search(pattern, path)))
    if re.search(pattern, path):
        return 'active'
    return ''