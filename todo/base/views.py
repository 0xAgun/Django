from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Task
class home(ListView):
    model = Task # importing the model
    context_object_name = 'tasks' #change the default object name

class taskdetail(DetailView):
    model = Task
    context_object_name = 'task' #change the default object name
    template_name = 'base/task.html' #this here change the default page name
    