from rest_framework import serializers
from .models import  FingersModel
class FingerSerializer(serializers.ModelSerializer):
    class Meta:
        model = FingersModel
        fields = '__all__'