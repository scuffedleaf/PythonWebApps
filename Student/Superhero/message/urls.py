from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [

    # Message
    path("message/", MessageListView.as_view(), name="message_list"),
    path("message/<int:pk>", MessageDetailView.as_view(), name="message_detail"),
    path("message/add", MessageCreateView.as_view(), name="message_add"),
    path("message/<int:pk>/", MessageUpdateView.as_view(), name="message_edit"),
    path("message/<int:pk>/delete",
         MessageDeleteView.as_view(), name="message_delete"),

]
