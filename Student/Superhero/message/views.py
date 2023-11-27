from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from .models import Message


class MessageListView(ListView):
    template_name = "message/list.html"
    model = Message
    context_object_name = "messages"


class MessageDetailView(DetailView):
    template_name = "message/detail.html"
    model = Message
    context_object_name = "message"


class MessageCreateView(LoginRequiredMixin, CreateView):
    template_name = "message/add.html"
    model = Message
    fields = "__all__"


class MessageUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "message/edit.html"
    model = Message
    fields = "__all__"


class MessageDeleteView(LoginRequiredMixin, DeleteView):
    model = Message
    template_name = "message/delete.html"
    success_url = reverse_lazy("message_list")
