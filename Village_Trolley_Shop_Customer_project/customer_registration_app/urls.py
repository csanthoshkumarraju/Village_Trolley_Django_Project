from django.urls import path
from . import views
urlpatterns = [
    path('customer_registartion_fun/',views.customer_registartion_fun,name='customer_registartion_fun')
]
