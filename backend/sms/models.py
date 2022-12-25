from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
from django.core.validators import MinLengthValidator
from django.db import models

from .utils import format_phonenumber
from .validators import validate_phone_number


class Message(models.Model):
    author = models.ForeignKey(verbose_name="Создатель", to=User, on_delete=models.CASCADE)
    text = models.TextField(verbose_name="Содержимое", max_length=600, validators=[
        MinLengthValidator(16, 'Поле должно содержать как минимум 16 символов.')
    ])

    send_to = ArrayField(models.CharField(max_length=17, blank=False, null=False, unique=True),
                         blank=False,
                         null=False,
                         size=16)

    is_sent = models.BooleanField(verbose_name="Сообщение разослано", default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def clean(self):
        if self.send_to:
            for idx, phone in enumerate(self.send_to):
                validate_phone_number(phone)
                print(idx, format_phonenumber(phone))
                self.send_to.__setitem__(idx, format_phonenumber(phone))

    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)

    def __str__(self):
        return f"Author={self.author.username}, text={self.text:10}..."

    class Meta:
        managed = True
        verbose_name = "Сообщение"
        verbose_name_plural = "Сообщения"
        db_table = "messages"
