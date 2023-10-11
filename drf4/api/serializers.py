from rest_framework import serializers
from .models import Student

# Validator
def start_with_r(value):
    if value[0].lower() != 'r':
        raise serializers.ValidationError("Name Must be start with 'R' letter")
    return value

class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100, validators = [start_with_r])
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=100)
    
    # To create data
    def create(self, validated_data):
        return Student.objects.create(**validated_data)
    
    # To update data
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.roll = validated_data.get('roll', instance.roll)
        instance.city = validated_data.get('city', instance.city)
        instance.save()
        return instance
    
    # Validation of a field
    def validate_roll(self, value):
        if value >= 200:
            raise serializers.ValidationError('Seat full. Try later.')
        return value
    
    # Validation of a object
    def validate(self, data):
        name = data.get('name')
        city = data.get('city')
        if name.lower() == 'limon' and city.lower() != 'lalmonirhat':
            raise serializers.ValidationError('City must be Lalmonirhat')
        return data
