from django.urls import path
from . import views
urlpatterns = [
    path('shop_owner_analytics/<int:shop_owner_id>/',views.shop_owner_analytics,name='shop_owner_analytics')
]

