from django.db import models

# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=30, unique=True)


class Task(models.Model):
    description= models.CharField(max_length=255)
    tags = models.ManyToManyField(Tag)


class Comment(models.Model): # new table for the same project
    # id will be set for us 
    body= models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)

# lines 11-13 are all attributes meaning coloumns of that table
# line 13 lets django know that this coloum is connected to the table on line 5 (foreign key)


    