from django.urls import path
from . import views

urlpatterns = [
    path('shop_owner_registration/', views.shop_owner_registration, name='shop_owner_registration'),  # Example URL pattern
    # Add more URL patterns as needed
]
