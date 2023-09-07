from django.db import models

# Create your models here.

class Information(models.Model):
    slack_name = models.CharField(max_length=100)
    current_day = models.DateTimeField()
    current_utc_time = models.DateTimeField()
    track = models.CharField(default="backend")
    github    
    
