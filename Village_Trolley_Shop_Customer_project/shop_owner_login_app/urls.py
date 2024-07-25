from django.urls import path
from . import views

urlpatterns = [
    path('shop_owner_login_view/', views.shop_owner_login_view, name='shop_owner_login_view'),
    # Define other URLs as needed
]