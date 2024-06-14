from django.test import TestCase,SimpleTestCase, Client
from django.urls import reverse, resolve
from .views import *
from .forms import TodoForms
from .models import Todo
from django.contrib.auth.models import User
from datetime import datetime
# Create your tests here.

class TestTodoUrl(SimpleTestCase):
    def test_list(self):
        url = reverse('todo:list')
        self.assertEqual(resolve(url).func.view_class, TodoListView)
        
    def test_delete(self):
        url = reverse('todo:delete',kwargs={'pk':1})
        self.assertEqual(resolve(url).func.view_class, DeleteView)
    
    def test_complete(self):
        url = reverse('todo:complete',kwargs={'pk':1})
        self.assertEqual(resolve(url).func.view_class,CompleteView)
class TestFormTodo(TestCase):
    def test_todo(self):
        form = TodoForms(data={
            'task':'say goodbye'           
        })
        self.assertTrue(form.is_valid())
        
class TestModelTodo(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='test', password='123456789')
        
    def test_model(self):
        
        obj = Todo.objects.create(
            user = self.user,
            task = 'test',
            complete = True,
            created_date = datetime.now()
        )
        self.assertTrue(Todo.objects.filter(pk=obj.id).exists(), True)
        
        
class TestView(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='test', password='123456789ali')
        
    
    def test_status_code(self):
        self.client.force_login(self.user)
        url = reverse('todo:list')
        response = self.client.get(url)
        self.assertEqual(response.status_code,200 )
        self.assertTemplateUsed(response,template_name="to-do-list.html" )
    