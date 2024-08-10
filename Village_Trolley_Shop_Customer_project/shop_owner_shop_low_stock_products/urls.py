from django.urls import path
from . import views

urlpatterns = [
     path('low_stock_products/<int:shop_owner_id>/', views.low_stock_products, name='low_stock_products'),
]