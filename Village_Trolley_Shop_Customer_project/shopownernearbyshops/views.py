from django.shortcuts import render,get_object_or_404
from shop_owner_registration_app.models import shop_owner_registration_model


def shop_owner_nearby_shops(request,shop_owner_id):
    shop_user_name = get_object_or_404(shop_owner_registration_model, pk=shop_owner_id)
    context = { 'shop_owner_first_name': shop_user_name.shop_owner_first_name,
                'shop_owner_last_name': shop_user_name.shop_owner_last_name,
                'shop_owner_shop_name': shop_user_name.shop_owner_shop_name,
                'shop_owner_id': shop_owner_id,
                }
    return render(request,'shopownernearbystores.html',context)

