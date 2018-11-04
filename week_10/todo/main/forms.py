from django.forms import ModelForm
from main.models import Task


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ('title', 'due_to','mark')
class TaskUpdateForm(ModelForm):
    class Meta:
        model=Task
        fields = ('title','due_to','mark')
    