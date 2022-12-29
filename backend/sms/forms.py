from django import forms
from django.contrib.postgres.forms import SimpleArrayField

from core.forms import BaseStyledForm
from .models import Message


class CreateMessageForm(BaseStyledForm):
    send_to = SimpleArrayField(forms.CharField(), label="Отправить на",
                               widget=forms.TextInput(attrs={"placeholder": "Номера, разделенные запятыми"}),
                               required=True)

    class Meta:
        model = Message
        fields = ('text', 'send_to')
