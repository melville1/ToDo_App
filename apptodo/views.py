from django.shortcuts import redirect, render
from django.views import View
from apptodo.models import Task, Comment 
from apptodo.forms import TaskForm, CommentForm


'''
HomeView functions as the site's homepage, listing out all task objects in the database
and linking out to each one's detail view

'''

class HomeView(View):
    def get(self, request):
        ''' The content required to render the homepage '''
        tasks = Task.objects.all()
        task_form = TaskForm()

        html_data = {
            'task_list': tasks,
            'form': task_form
        }
        return render(
        request= request,
        template_name= "index.html",
        context= html_data
        )


    def post(self, request):
       
        task_form = TaskForm(request.POST)
        task_form.save()


        return redirect('home')


class TaskDetailView(View):
    def get(self,request, task_id):
        task = Task.objects.get(id=task_id)

        task_form = TaskForm(instance=task)

        comments = Comment.objects.filter(task=task)

        comment_form = CommentForm(task_object=task)

        html_data = {
            'task_object': task,
            'form': task_form,
            'comment_list': comments,
            'comment_form': comment_form,

        }
        
        return render(
        request= request,
        template_name= "detail.html",
        context= html_data
        )

    def post(self, request, task_id):
        task= Task.objects.get(id=task_id)

        if 'update' in request.POST:
            task_form= TaskForm(request.POST, instance=task)
            task_form.save()
        elif 'delete' in request.POST:
            task.delete()
        elif 'add' in request.POST:
            comment_form=CommentForm(request.POST, task_object=task)
            comment_form.save()

            return redirect('task_detail', task.id)

        return redirect('home')

    


        







       




