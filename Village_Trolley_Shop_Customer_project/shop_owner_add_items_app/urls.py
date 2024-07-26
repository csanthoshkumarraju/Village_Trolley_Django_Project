from django.urls import path
from . import views

urlpatterns = [
     path('shop_owner_add_items/<int:shop_owner_id>/', views.add_items_for_shop_owner, name='shop_owner_add_items'),
]
