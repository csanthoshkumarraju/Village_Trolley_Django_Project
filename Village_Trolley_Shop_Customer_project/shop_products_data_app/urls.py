from django.urls import path
from . import views

urlpatterns = [
     path('shop_owner_products_data/<int:shop_owner_id>/',views.shop_owner_products_data,name='shop_owner_products_data')
]
