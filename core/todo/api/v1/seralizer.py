from rest_framework import serializers
from todo.models import Todo
from django.contrib.auth.models import User



class TodoSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(slug_field='username',read_only=True)
    class Meta():
        model = Todo
        fields = [ 'id','user','task', 'complete', 'created_date', 'updated_date']
   
    
    def create(self, validated_data):
        validated_data['user'] = User.objects.get(id=self.context.get('request').user.id)
        return super().create(validated_data)
    
    