from django.urls import path
from . import views

urlpatterns = [
    path('customer_login_fun',views.customer_login_fun,name='customer_login_fun')
]
