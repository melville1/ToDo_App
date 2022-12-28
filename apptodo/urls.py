from django.urls import path
from apptodo.views import HomeView, TaskDetailView


urlpatterns = [ 
    path('', HomeView.as_view(), name='home' ),
    path('<int:task_id>' , TaskDetailView.as_view(), name='task_detail' ),
    
    ]

    # line 7 where we see <int:task_id>  what this is doing is saving the id number of whatever was clicked
    # rememeber each row has an id number that is created for it. line 7 says hey after the user is in the homepage
    # and then clicks on a item(row) save that number(id) and then take them to the view in this ex. it is the 
    # TaskDetailView