from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.RegisterCreateView.as_view(), name='register'),
    path('login/', views.LoginFormView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    
    
]