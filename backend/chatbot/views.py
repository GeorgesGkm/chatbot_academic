from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import StudentFAQ
from .serializers import StudentFAQSerializer

class StudentFAQViewSet(viewsets.ModelViewSet):
    queryset = StudentFAQ.objects.all()
    serializer_class = StudentFAQSerializer