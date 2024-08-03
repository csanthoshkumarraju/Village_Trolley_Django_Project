from django.urls import path
from . import views

urlpatterns = [
    path('submit-rating/', views.shop_rating_view, name='submit_rating'),
]
