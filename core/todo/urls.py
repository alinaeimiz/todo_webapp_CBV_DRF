from django.urls import path
from . import views

app_name = 'todo'

urlpatterns = [
   path('', views.TodoListView.as_view(), name='list'),
   path('<int:pk>/', views.CompleteView.as_view(), name='complete'),
]