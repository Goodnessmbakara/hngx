"""serializer for the get_endpoint appp"""
from rest_framework import serializers
from .models import Person

def validate_unique_name(value):
    if Person.objects.filter(name=value).exists():
        raise serializers.ValidationError("This name already exists. Please choose a different name.")

class PersonSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=255, validators=[validate_unique_name])

    class Meta:
        model = Person
        fields = '__all__'

