from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    # name = serializers.CharField(read_only=True)
    class Meta:
        model = Student
        fields = ['name', 'roll', 'city']
        # read_only_fields = ['roll'] # Multiple field name can be putted here  
        extra_kwargs = {'name' : {'read_only' : True}, 'roll' : {'read_only' : True}}
    
