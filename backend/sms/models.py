from django.db import models
from django.contrib.auth.models import User


class SMS(models.Model):
    author = models.ForeignKey(verbose_name="Создатель", to=User, on_delete=models.CASCADE)
    text = models.TextField(verbose_name="Содержимое сообщения", max_length=600)

    class Meta:
        db_table = 'dbo.messages'
        verbose_name = "Сообщение"
        verbose_name_plural = "Сообщения"
