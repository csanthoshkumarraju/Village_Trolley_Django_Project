from django.urls import path
from . import views

urlpatterns = [
    path('update_password/', views.update_password, name='customer_update_password'),  # Example URL pattern
    # Add more URL patterns as needed
]