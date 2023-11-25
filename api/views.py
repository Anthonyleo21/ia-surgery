#from django.shortcuts import render
from rest_framework import viewsets
from .serializer import SurgerySerializer
from .models import Surgery

# Create your views here.

class SurgeryViewSet(viewsets.ModelViewSet):
    queryset=Surgery.objects.all()
    serializer_class = SurgerySerializer
