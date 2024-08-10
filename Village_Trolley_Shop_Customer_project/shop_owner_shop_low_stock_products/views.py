from django.shortcuts import render,get_object_or_404
from shop_owner_registration_app.models import shop_owner_registration_model
from shop_owner_add_items_app.models import shop_owner_add_items
# Create your views here.

def low_stock_products(request, shop_owner_id):
    shop_user_name = get_object_or_404(shop_owner_registration_model, pk=shop_owner_id)
    
    low_stock_items = shop_owner_add_items.objects.filter(
        shop_user_name=shop_user_name,
        product_qunatity__lt=21
    )
    

    context = {
        'shop_owner': shop_user_name,
        'shop_owner_id': shop_owner_id,
        'shop_owner_first_name': shop_user_name.shop_owner_first_name,
        'shop_owner_last_name': shop_user_name.shop_owner_last_name,
        'shop_owner_shop_name': shop_user_name.shop_owner_shop_name,
        'low_stock_items': low_stock_items,
    }
    return render(request, 'lowstockproducts.html',context)
