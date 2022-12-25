from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic import ListView

from .forms import CreateMessageForm
from .models import Message


class MessagesListView(LoginRequiredMixin, ListView):
    model = Message
    template_name = "sms/messages-list.html"
    context_object_name = "messages"
    paginate_by = 10

    def get_queryset(self):
        return Message.objects.filter(author_id=self.request.user.id).order_by("-created_at")


class MessageCreateView(LoginRequiredMixin, CreateView):
    model = Message
    template_name = "sms/message-add.html"
    form_class = CreateMessageForm
    success_url = reverse_lazy("url_messages_list")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
