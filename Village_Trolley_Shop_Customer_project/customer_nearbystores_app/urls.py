from django.urls import path
from .views import customer_search_nearby_shops,customer_selected_shop_owner_products_data

urlpatterns = [
    path('customer_search_nearby_shops/',customer_search_nearby_shops,name='customer_search_nearby_shops'),
    path('customer_selected_shop_owner_products_data/<int:shop_owner_id>/',customer_selected_shop_owner_products_data, name='customer_selected_shop_owner_products_data'),
]


# urlpatterns = [
#     path('shop_owner_nearby_shops/<int:shop_owner_id>/', views.shop_owner_nearby_shops, name='shop_owner_nearby_shops'),
#     path('selected_shop_owner_products/<int:shop_owner_id>/', views.selected_shop_owner_products_data, name='selected_shop_owner_products'),
# ]