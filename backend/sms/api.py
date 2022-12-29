from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from .models import Message
from .serializers import MessageSerializer, CreateMessageSerializer


class MessageAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, id: int = None):
        """
        If the id is provided, return the message with that id, otherwise return all messages

        :param id: int = None
        :type id: int
        :return: A list of messages or a single message.
        """
        if id:
            msg = get_object_or_404(Message, id=id, author_id=request.user.id)
            s = MessageSerializer(msg)
        else:
            msgs = Message.objects.filter(author_id=request.user.id)
            s = MessageSerializer(msgs, many=True)

        return Response(s.data)

    def post(self, request):
        """
        The function takes a request, serializes the request data, checks if the serialized data is valid, saves the
        serialized data, and returns the serialized data

        send_to - массив строк с номерами формата: +7xxxxxxxxxx

        :return: The serializer is returning the data that was saved.
        """
        s = CreateMessageSerializer(data=request.data)
        if s.is_valid():
            s.save(author=request.user)
            return Response(s.data)

        return Response(s.errors, status=status.HTTP_400_BAD_REQUEST)

