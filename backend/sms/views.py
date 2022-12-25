from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
from django.views.generic import ListView

from .models import Message


class MessagesListView(LoginRequiredMixin, ListView):
    model = Message
    template_name = "sms/messages-list.html"
    context_object_name = "messages"
    paginate_by = 5

    def get_queryset(self):
        return Message.objects.filter(author_id=self.request.user.id).order_by("-created_at")


class MessageCreateView(CreateView):
    pass
