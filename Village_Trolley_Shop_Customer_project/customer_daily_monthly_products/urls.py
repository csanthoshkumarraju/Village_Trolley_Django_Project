from django.urls import path
from . import views

urlpatterns = [
    path('customer_daily_monthly_purchasing_data/', views.customer_daily_monthly_purchasing_data, name='customer_daily_monthly_purchasing_data'),
]