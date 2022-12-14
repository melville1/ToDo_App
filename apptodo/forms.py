from django.forms import ModelForm
from apptodo.models import Task, Comment


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['description']


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['body']

# the form will be created with a task. we need to pull that task out
# and keep track of it 

    def __init__(self, *args, **kwargs):
        task = kwargs.pop('task_object')
        super().__init__(*args, **kwargs)

    #self.instance is the comment we are creating with this form

        self.instance.task = task

    
    #comment_form = CommentForm(task_object=Task.objects.first())



