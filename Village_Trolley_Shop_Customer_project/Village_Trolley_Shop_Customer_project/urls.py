"""
URL configuration for Village_Trolley_Shop_Customer_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('introduction_app.urls')),
    path('', include('shop_owner_registration_app.urls')),
    path('', include('shop_owner_login_app.urls')),
    path('', include('shop_owner_forgot_pwd_app.urls')),
    path('', include('shop_owner_add_items_app.urls')),
    path('', include('shop_products_data_app.urls')),
    path('', include('customer_registration_app.urls')),
    path('', include('customer_login_app.urls')),
    path('', include('customer_reset_password_app.urls')),
    path('', include('shopownernearbyshops.urls')),
    path('', include('shop_owner_analytics_app.urls')),
    path('', include('customer_nearbystores_app.urls')),
    path('', include('customer_nearbystores_rating_app.urls')),
    path('', include('shop_owner_billing_app.urls')),
]


