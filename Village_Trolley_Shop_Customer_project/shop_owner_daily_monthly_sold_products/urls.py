from django.urls import path
from . import views

urlpatterns = [
     path('daily_monthly_sold_products/<int:shop_owner_id>/', views.daily_monthly_sold_products, name='daily_monthly_sold_products'),
]
