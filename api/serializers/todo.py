from rest_framework import serializers, viewsets

from todo.models import Todo

class TodoSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Todo
        fields = [
            "user",
            "title",
            "description",
            "is_completed",
            "datetime_completed",
        ]
   
class TodoViewSet(viewsets.ModelViewSet):
    
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

