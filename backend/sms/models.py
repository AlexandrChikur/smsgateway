from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
from django.db import models

from .validators import validate_phone_number


class Message(models.Model):
    author = models.ForeignKey(verbose_name="Создатель", to=User, on_delete=models.CASCADE)
    text = models.TextField(verbose_name="Содержимое", max_length=600)

    send_to = ArrayField(models.CharField(validators=[validate_phone_number],
                                          max_length=17,
                                          blank=False,
                                          null=False),
                         blank=False,
                         null=False,
                         size=16)

    is_sent = models.BooleanField(verbose_name="Сообщение разослано", default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Author={self.author.username}, text={self.text:10}..."

    class Meta:
        managed = True
        verbose_name = "Сообщение"
        verbose_name_plural = "Сообщения"
        db_table = "messages"
