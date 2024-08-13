from django.urls import path
from . import views

urlpatterns = [
    path('shop_owner_nearby_shops/<int:shop_owner_id>/', views.shop_owner_nearby_shops, name='shop_owner_nearby_shops'),
    path('selected_shop_owner_products/<int:n_shop_owner_id>/', views.selected_shop_owner_products_data, name='selected_shop_owner_products'),
]
