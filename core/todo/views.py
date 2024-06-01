from django.db.models.query import QuerySet
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DeleteView, FormView
from django.contrib import messages 
from django.views import View
from .models import Todo
from .forms import TodoForms
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here. 


class TodoListView(LoginRequiredMixin,ListView):
    template_name = "to-do-list.html"
    redirect_field_name = 'login'
    def get_queryset(self):
        object = Todo.objects.filter(user=self.request.user)
        return object



class CompleteView(LoginRequiredMixin,View):
    model = Todo
    success_url = reverse_lazy("todo:list")
    redirect_field_name = 'login'
    def get(self , request, *args, **kwargs):
        obj = Todo.objects.get(id= kwargs.get('pk'))
        obj.complete = True
        obj.save()
        messages.success(request,'your task is finished')
        return redirect('/')
        
        
class DeleteView(LoginRequiredMixin,View):
    model = Todo
    success_url = reverse_lazy("todo:list")
    redirect_field_name = 'login'
    def get(self , request, *args, **kwargs):
        obj = Todo.objects.get(id= kwargs.get('pk'))
        obj.delete()
        messages.success(request,'your task is deleted')
        return redirect('/')


class TaskFormViews(LoginRequiredMixin,FormView):
    form_class = TodoForms
    template_name = 'to-do-list.html'
    success_url = reverse_lazy("todo:list")
    redirect_field_name = 'login'
    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        return super().form_valid(form)