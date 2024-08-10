from django.urls import path
from . import views
urlpatterns = [
    path('shop_owner_billing/<int:shop_owner_id>/',views.shop_owner_billing,name='shop_owner_billing')
]
