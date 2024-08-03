from django.shortcuts import render,get_object_or_404
from shop_owner_registration_app.models import shop_owner_registration_model
from shop_owner_add_items_app.models import shop_owner_add_items
from .forms import ShopSearchForm

# def shop_owner_nearby_shops(request,shop_owner_id):
#     shop_user_name = get_object_or_404(shop_owner_registration_model, pk=shop_owner_id)
#     context = { 'shop_owner_first_name': shop_user_name.shop_owner_first_name,
#                 'shop_owner_last_name': shop_user_name.shop_owner_last_name,
#                 'shop_owner_shop_name': shop_user_name.shop_owner_shop_name,
#                 'shop_owner_village_name': shop_user_name.shop_owner_village_name,
#                 'shop_owner_id': shop_owner_id,
#                 }
#     return render(request,'shopownernearbystores.html',context)




# def shop_owner_nearby_shops(request, shop_owner_id):
#     # Retrieve the specific shop owner
#     shop_owner = get_object_or_404(shop_owner_registration_model, pk=shop_owner_id)
    
#     # Initialize the search form
#     form = ShopSearchForm(request.GET or None)
#     shops = []

#     # If the form is valid, filter shops based on the village name
#     if form.is_valid():
#         village_name = form.cleaned_data.get('village_name')
#         if village_name:
#             shops = shop_owner_registration_model.objects.filter(shop_owner_village_name__icontains=village_name)

#     # Prepare the context with both shop owner details and search results
#     context = {
#         'form': form,
#         'shops': shops,
#         'shop_owner_first_name': shop_owner.shop_owner_first_name,
#         'shop_owner_last_name': shop_owner.shop_owner_last_name,
#         'shop_owner_shop_name': shop_owner.shop_owner_shop_name,
#         'shop_owner_village_name': shop_owner.shop_owner_village_name,
#         'shop_owner_id': shop_owner_id,
#     }
    
#     return render(request, 'shopownernearbystores.html', context)

def shop_owner_nearby_shops(request, shop_owner_id):
    # Retrieve the specific shop owner
    shop_owner = get_object_or_404(shop_owner_registration_model, pk=shop_owner_id)
    
    # Initialize the search form
    form = ShopSearchForm(request.GET or None)
    shops = []

    # Print the request GET data for debugging
    # print("Request GET data:", request.GET)

    # If the form is valid, filter shops based on the village name
    if form.is_valid():
        village_name = form.cleaned_data.get('village_name')
        # print("Village Name:", village_name)
        if village_name:
            shops = shop_owner_registration_model.objects.filter(shop_owner_village_name__icontains=village_name)
            # print("Shops found:", shops)
    # else:
        # print("Form errors:", form.errors)

    # Prepare the context with both shop owner details and search results
    context = {
        'form': form,
        'shops': shops,
        'shop_owner_first_name': shop_owner.shop_owner_first_name,
        'shop_owner_last_name': shop_owner.shop_owner_last_name,
        'shop_owner_shop_name': shop_owner.shop_owner_shop_name,
        'shop_owner_village_name': shop_owner.shop_owner_village_name,
        'shop_owner_id': shop_owner_id,
    }
    
    return render(request, 'shopownernearbystores.html', context)

def selected_shop_owner_products_data(request, shop_owner_id):
    shop_user_name = get_object_or_404(shop_owner_registration_model, pk=shop_owner_id)
    shop_owner_products = shop_owner_add_items.objects.filter(shop_user_name=shop_user_name)

    context = {
        'shop_owner_first_name': shop_user_name.shop_owner_first_name,
        'shop_owner_last_name': shop_user_name.shop_owner_last_name,
        'shop_owner_shop_name': shop_user_name.shop_owner_shop_name,
        'shop_owner_id': shop_owner_id,
        'shop_owner_products': shop_owner_products,
    }

    return render(request, 'shop_owner_nearby_shop_products.html', context)
