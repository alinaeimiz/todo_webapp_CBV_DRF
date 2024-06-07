from rest_framework import viewsets
from rest_framework.response import Response
from .seralizer import TodoSerializer
from todo.models import Todo
from rest_framework.permissions import IsAuthenticated,IsAdminUser

class TodoViewset(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = TodoSerializer
    
    
    
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset, many=True)
        return super().list(request, *args, **kwargs)
    
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(user=self.request.user)
    
    
class DetailViewset(viewsets.ModelViewSet):
    permission_classes=[IsAdminUser]
    serializer_class=TodoSerializer
    queryset = Todo.objects.all()
    
 

   