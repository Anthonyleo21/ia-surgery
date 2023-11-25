from rest_framework import serializers
from .models import Surgery

class SurgerySerializer(serializers.ModelSerializer):
    class Meta:
        model=Surgery
        #fields = ('fullname', 'nickname')
        fields = '__all__'