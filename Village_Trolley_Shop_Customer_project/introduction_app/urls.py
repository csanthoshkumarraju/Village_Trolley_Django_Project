from django.urls import path
from . import views

urlpatterns = [
    path('', views.introduction, name='introduction'),  # Example URL pattern
    path('common_register_page/', views.common_register_page, name='common_register_page'),  # Example URL pattern
    # Add more URL patterns as needed
]