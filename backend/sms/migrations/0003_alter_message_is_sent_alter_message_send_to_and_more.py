# Generated by Django 4.1.4 on 2022-12-25 21:20

import django.contrib.postgres.fields
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("sms", "0002_remove_message_phone_number"),
    ]

    operations = [
        migrations.AlterField(
            model_name="message",
            name="is_sent",
            field=models.BooleanField(
                default=False, verbose_name="Сообщение разослано"
            ),
        ),
        migrations.AlterField(
            model_name="message",
            name="send_to",
            field=django.contrib.postgres.fields.ArrayField(
                base_field=models.CharField(max_length=17, unique=True), size=16
            ),
        ),
        migrations.AlterField(
            model_name="message",
            name="text",
            field=models.TextField(
                max_length=600,
                validators=[
                    django.core.validators.MinLengthValidator(
                        16, "Поле должно содержать как минимум 16 символов."
                    )
                ],
                verbose_name="Содержимое",
            ),
        ),
    ]
