from django.urls import path
from . import views

urlpatterns = [
    path('shop_owner_nearby_shops/<int:shop_owner_id>/', views.shop_owner_nearby_shops, name='shop_owner_nearby_shops'),
]
