from rest_framework import serializers
from .models import StudentFAQ

class StudentFAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentFAQ
        fields = ('question', 'answer')