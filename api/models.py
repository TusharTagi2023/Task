from django.db import models

# Create your models here.

class Worker (models.Model):
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)

class Unit (models.Model):
    name = models.CharField(max_length=255)
    worker= models.ForeignKey(Worker, on_delete=models.CASCADE, related_name='unit')

class Visit (models.Model):
    date_time = models.DateTimeField(auto_now_add=True)
    unit=models.ForeignKey(Unit, on_delete=models.CASCADE, related_name='visit')
    latitude=models.FloatField()
    longitude=models.FloatField()
    

