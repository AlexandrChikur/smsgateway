from django.urls import path, include
from .views import MessagesListView, MessageCreateView

urlpatterns = [
    path('', MessagesListView.as_view(), name="url_messages_list"),
    path('add/', MessageCreateView.as_view(), name="url_message_add"),
]