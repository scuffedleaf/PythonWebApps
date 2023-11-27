from django.db import models
from django.urls import reverse_lazy


class Message(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse_lazy("message_list")
