from django.shortcuts import render,get_object_or_404
from shop_owner_registration_app.models import shop_owner_registration_model
from shop_owner_add_items_app.models import shop_owner_add_items


# Create your views here.
def shop_owner_products_data(request,shop_owner_id):
    shop_user_name = get_object_or_404(shop_owner_registration_model, pk=shop_owner_id)
    shop_owner_products = shop_owner_add_items.objects.filter(shop_user_name=shop_user_name)
    context = {
                    'shop_owner_first_name': shop_user_name.shop_owner_first_name,
                    'shop_owner_last_name': shop_user_name.shop_owner_last_name,
                    'shop_owner_shop_name': shop_user_name.shop_owner_shop_name,
                    'shop_owner_id': shop_owner_id,
                    'shop_owner_products': shop_owner_products
                }

    return render(request,'shop_owner_data.html',context)

