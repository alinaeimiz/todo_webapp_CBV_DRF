from django import forms
from .models import Todo

class TodoForms(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['task']
        
    