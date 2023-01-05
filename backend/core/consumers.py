from djangochannelsrestframework import mixins
from djangochannelsrestframework.generics import GenericAsyncAPIConsumer, AsyncAPIConsumer
from channels.db import database_sync_to_async
from djangochannelsrestframework.observer import model_observer
from djangochannelsrestframework.observer.generics import (ObserverModelInstanceMixin, action)

from sms.models import Message
from sms.serializers import MessageSerializer


class MessageConsumer(mixins.PatchModelMixin,
                      ObserverModelInstanceMixin,
                      GenericAsyncAPIConsumer):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    async def accept(self, **kwargs):
        await super().accept()
        await self.message_activity.subscribe(author_id=self.scope['user'].id, a=3,b=3)

    async def disconnect(self, code):
        await self.send_json(
            {"message": "connection closed"}
        )
        await super().disconnect(code)

    @model_observer(Message)
    async def message_activity(self, message, observer=None, **kwargs):
        await self.send_json(message)

    @message_activity.serializer
    def message_activity(self, instance: Message, action, **kwargs):
        return dict(data=MessageSerializer(instance).data, action=action.value, pk=instance.pk)
