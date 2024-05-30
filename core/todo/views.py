from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views import View
from .models import Todo

# Create your views here. 


class TodoListView(ListView):
    model = Todo
    template_name = "to-do-list.html"



class CompleteView(View):
    model = Todo
    success_url = reverse_lazy("todo:list")
    
    def get(self , request, *args, **kwargs):
        obj = Todo.objects.get(id= kwargs.get('pk'))
        if obj.complete == True:
            obj.complete = False
            obj.save()
            return redirect('/')
        else:
            obj.complete = True
            obj.save()
            return redirect('/')