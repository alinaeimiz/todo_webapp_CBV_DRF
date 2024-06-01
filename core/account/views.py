from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import FormView
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.


class RegisterCreateView(FormView):
    form_class = UserCreationForm
    template_name = 'register.html'
    success_url = reverse_lazy('todo:list')
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class LoginFormView(FormView):
    form_class = AuthenticationForm
    template_name = "login.html"
    success_url = reverse_lazy('todo:list')

    def form_valid(self, form):
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(self.request, username=username, password=password)
        if user is not None:
            login(self.request, user)
        return super().form_valid(form)
  
class LogoutView(LoginRequiredMixin,View):
    redirect_field_name = 'login'
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('/account/login')
    