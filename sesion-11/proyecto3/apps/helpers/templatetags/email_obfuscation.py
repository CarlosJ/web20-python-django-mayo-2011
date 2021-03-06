#!/usr/bin/env python
# -*- encoding: utf8 -*-

from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter
@stringfilter
def email_obfuscation(value):
    return ''.join(["&#%d;" % ord(c) for c in value])

@register.simple_tag
def random_integer(min, max):
    from random import randint
    min = int(min)
    max = int(max)
    return str(randint(min, max))
