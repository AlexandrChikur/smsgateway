import phonenumbers
from django import template
from django.conf import settings

register = template.Library()


@register.filter(name='phonenumber_format')
def phonenumber_format(value):
    try:
        parsed = phonenumbers.parse(value, region=settings.DEFAULT_PHONE_REGION)
    except phonenumbers.NumberParseException:
        return f'invalid-number-{value}'
    return phonenumbers.format_number(parsed, phonenumbers.PhoneNumberFormat.RFC3966)
