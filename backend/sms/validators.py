import phonenumbers
from django.conf import settings
from django.contrib.postgres.validators import ValidationError


def validate_phone_number(number_string):
    try:
        number = phonenumbers.parse(number_string)
    except phonenumbers.NumberParseException:
        raise ValidationError(f"'{number_string}' не соответствует схеме номера")

    if not phonenumbers.is_valid_number_for_region(number, settings.DEFAULT_PHONE_REGION):
        raise ValidationError(
            f"Номер '{number_string}' не является валидным для заданного региона: \"{settings.DEFAULT_PHONE_REGION}\"")

    if not phonenumbers.is_valid_number(number):
        raise ValidationError(f"Номер '{number_string}' не является валидным")

    return number_string
