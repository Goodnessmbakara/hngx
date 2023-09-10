"""serializer for the get_endpoint appp"""
from rest_framework import serializers
from .models import Person

class PersonSerializer(serializers.ModelSerializer):
    """serializer foe the Person model"""
    class Meta:
        model = Person
        fields = ('id', 'name')

