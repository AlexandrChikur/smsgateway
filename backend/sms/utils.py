import phonenumbers
from django.conf import settings
from django.core.exceptions import ValidationError
from phonenumbers import PhoneNumberFormat


def format_phonenumber(number_str, fmt=PhoneNumberFormat.INTERNATIONAL):
    try:
        parsed = phonenumbers.parse(number_str, region=settings.DEFAULT_PHONE_REGION)
    except phonenumbers.NumberParseException:
        raise ValidationError(f"'{number_str}' не соответствует ни одной схеме номера")
    return phonenumbers.format_number(parsed, fmt)
