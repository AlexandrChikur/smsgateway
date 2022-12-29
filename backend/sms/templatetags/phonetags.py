from django import template

from sms.utils import format_phonenumber

register = template.Library()


@register.filter(name='phonenumber_format')
def phonenumber_format(value):
    return format_phonenumber(value)
