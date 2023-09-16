from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, RedirectView, UpdateView

from .models import ClassName


class ClassNameView(RedirectView):
    url = reverse_lazy('object_instance_list')


class ClassNameListView(ListView):
    template_name = 'object_instance/list.html'
    model = ClassName
    context_object_name = 'object_instances'


class ClassNameDetailView(DetailView):
    template_name = 'object_instance/detail.html'
    model = ClassName
    context_object_name = 'object_instance'

    # def get_context_data(self, **kwargs):
    #     kwargs = super().get_context_data(**kwargs)
    #     object_instance = kwargs.get('object_instance')
    #     kwargs['dependents'] = object_instance.dependents
    #     return kwargs


class ClassNameCreateView(LoginRequiredMixin, CreateView):
    template_name = "object_instance/add.html"
    model = ClassName
    fields = '__all__'

    # def form_valid(self, form):
    #     form.instance.book = 1
    #     form.instance.author = Person.get_me(self.request.user)
    #     return super().form_valid(form)


class ClassNameUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "object_instance/edit.html"
    model = ClassName
    fields = '__all__'


class ClassNameDeleteView(LoginRequiredMixin, DeleteView):
    model = ClassName
    template_name = 'object_instance/delete.html'
    success_url = reverse_lazy('object_instance_list')
