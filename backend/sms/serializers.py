from rest_framework import serializers

from .models import Message
from .validators import validate_phone_number


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        exclude = ('author',)


class CreateMessageSerializer(serializers.ModelSerializer):
    send_to = serializers.ListField(child=serializers.CharField())

    class Meta:
        model = Message
        fields = ('text', 'send_to')
