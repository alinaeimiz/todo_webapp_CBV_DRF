from rest_framework import routers
from .views import TodoViewset, DetailViewset

router = routers.DefaultRouter()
router.register('todo',TodoViewset, basename='todo-list')
router.register('todo-detail',DetailViewset, basename='todo-detail')

urlpatterns = []

urlpatterns += router.urls