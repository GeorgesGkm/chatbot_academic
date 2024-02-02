from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StudentFAQViewSet


urlpatterns = [
    path('', StudentFAQViewSet.as_view(), name='student'),

]