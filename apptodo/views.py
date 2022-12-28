from django.shortcuts import redirect, render # redirect sends  our post back to the get method
from django.views import View
from apptodo.models import Task, Comment, Tag 
from apptodo.forms import TaskForm, CommentForm, TagForm


'''
HomeView functions as the site's homepage, listing out all task objects in the database
and linking out to each one's detail view

'''

class HomeView(View): # this is an empty get page and no repeated code after the post
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


    def post(self, request): # take input from the user and saving it to the database
       
        task_form = TaskForm(request.POST)
        task_form.save()
        
# this is where the logic for the form takes place
# line 32 request is coming from the html form tag
# the post method executes only when the request has data 
# data gets sent once the create button gets pressed
# line 33 finalizes the process by creating a new object in the Task table that we created
#when we say create new object we mean add a new item/row to the table

        return redirect('home')
# after the item is saved to the database then it redirects the user to home 
# which is what we decided to name our homepage


class TaskDetailView(View):
    def get(self,request, task_id): # the task_id comes from the url and makes it specific to that number
        task = Task.objects.get(id=task_id) # here we are saving the id to a variable so we can only view deal with that id

        task_form = TaskForm(instance=task) # which instance which row are talking about when populating this form. here we called it task
        #we want to start this page with the taskform info we just clicked.

        comments = Comment.objects.filter(task=task) #this specifies that i want to get the commenrs related to that id 

        comment_form = CommentForm(task_object=task)

        # tags =task.tags.all()
        # tag_form = TagForm() # this wont work because it create the tag but it wont assign it to the specific id/task

        tags = Tag.objects.filter(task=task)
        tag_form = TagForm(instance=task)

        #tags = Tag.objects.filter(id=task_id) # this wont work because django does not know what id we are talking about. 
        #tag_form = TagForm(instance=task)

        html_data = {
            'task_object': task,
            'form': task_form,
            'tag_form': tag_form,
            'comment_list': comments, 
            'comment_form': comment_form,
            'tags': tags,
            #'tag_form': tag_form

        }
        
        return render(
        request= request,
        template_name= "detail.html",
        context= html_data
        )

    def post(self, request, task_id): # signature parameters
        task= Task.objects.get(id=task_id)
        task_form = TaskForm(request.POST,instance=task) # make changes to this specific id/task/row all the same 

        if 'update' in request.POST: # the logic for when they click the update button
            task_form= TaskForm(request.POST, instance=task)
            task_form.save()
        elif 'delete' in request.POST: # the logic for when they click delete button
            task.delete()
        elif 'add' in request.POST:
            comment_form=CommentForm(request.POST, task_object=task)
            comment_form.save()

            return redirect('task_detail', task.id)
        elif 'tag' in request.POST:
            tag_form = TagForm(request.POST)
            tag_form.save(task)
            
            return redirect('task_detail', task.id)

        return redirect('home')

    


        







       




