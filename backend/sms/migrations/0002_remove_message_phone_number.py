# Generated by Django 4.1.4 on 2022-12-24 23:21

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("sms", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="message",
            name="phone_number",
        ),
    ]
