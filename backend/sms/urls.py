from django.urls import path

from sms import views

urlpatterns = [
    path('all/', views.MessagesListView.as_view(), name="url_messages_list"),
    path('create/', views.MessageCreateView.as_view(), name="url_message_add"),
]
