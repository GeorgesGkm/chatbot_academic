from django.db import models

class StudentFAQ(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()
