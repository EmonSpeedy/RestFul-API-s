from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    # Validator
    def start_with_r(value):
        if value[0].lower() != 'r':
            raise serializers.ValidationError("Name Must be start with 'R' letter")
        return value
    
    name = serializers.CharField(validators=[start_with_r])
    class Meta:
        model = Student
        fields = ['name', 'roll', 'city']
    # Validation of a field
    def validate_roll(self, value):
        if value >= 200:
            raise serializers.ValidationError('Seat full. Try later.')
        return value
    
    # Validation of a object
    # def validate(self, data):
    #     name = data.get('name')
    #     city = data.get('city')
    #     if name.lower() == 'safa' and city.lower() != 'bahaddarhat':
    #         raise serializers.ValidationError('City must be Bahaddarhat')
    #     return data
