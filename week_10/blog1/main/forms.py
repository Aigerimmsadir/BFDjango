from django.forms import ModelForm
from main.models import Post,Comment


class PostForm(ModelForm):
    class Meta:
        model = Post
        # fields = ('title', 'created', 'author','content')
        fields = ('title','content')
class PostUpdateForm(ModelForm):
    class Meta:
        model=Post
        fields = ('title','content')
        def __init__(self,task, arg):
            super(TaskUpdateForm, self).__init__()
            self.arg = arg
class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)
