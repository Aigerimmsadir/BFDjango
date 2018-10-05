from django.forms import ModelForm
from main.models import Task,Owner


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ('title', 'created', 'due_to','owner','mark')
