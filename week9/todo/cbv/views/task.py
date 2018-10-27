from django.urls import reverse_lazy
from django.views.generic import (
    TemplateView,
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.contrib.auth.mixins import LoginRequiredMixin

from cbv.models import Task
from cbv.forms import TaskForm
import datetime

class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = 'tasks'


class TaskDetailView(LoginRequiredMixin, DetailView):
    model = Task


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    fields = ['title','due_to','mark']
    success_url = reverse_lazy('cbv:task_list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        form.instance.created = datetime.datetime.now()
        return super().form_valid(form)


class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ['title','due_to','mark']
    success_url = reverse_lazy('cbv:task_list')

    def get_queryset(self):
        return Task.objects.for_user(user=self.request.user)
    def form_valid(self, form):
        form.instance.owner = self.request.user
        form.instance.created = datetime.datetime.now()
        return super().form_valid(form)

class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    success_url = reverse_lazy('cbv:task_list')

    def get_queryset(self):
        return Task.objects.for_user(user=self.request.user)