"""model for the get_endpoint app"""
from django.db import models

class Person(models.Model):
    """ 
    Person model

    """
    name = models.CharField(max_length=100)

