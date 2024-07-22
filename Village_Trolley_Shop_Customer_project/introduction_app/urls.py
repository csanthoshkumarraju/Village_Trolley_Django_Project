from django.urls import path
from . import views

urlpatterns = [
    path('', views.introduction, name='introduction'),  # Example URL pattern
    # Add more URL patterns as needed
]