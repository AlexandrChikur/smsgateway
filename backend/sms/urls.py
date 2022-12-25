from django.urls import path

from .views import MessageCreateView
from .views import MessagesListView

urlpatterns = [
    path('', MessagesListView.as_view(), name="url_messages_list"),
    path('add/', MessageCreateView.as_view(), name="url_message_add"),
]
