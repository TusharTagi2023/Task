from rest_framework import serializers
from .models import *



class WorkerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Worker
        fields = '__all__'

class UnitSerializer(serializers.ModelSerializer):
    class Meta:
        model=Unit
        fields = ['id','name']

class VisitSerializer(serializers.ModelSerializer):
    class Meta:
        model=Visit
        fields = ['id','date_time']
