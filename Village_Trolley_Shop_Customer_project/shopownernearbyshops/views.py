from django.shortcuts import render,get_object_or_404
from shop_owner_registration_app.models import shop_owner_registration_model
from shop_owner_add_items_app.models import shop_owner_add_items
from .forms import ShopSearchForm
from django.db.models import Avg
from customer_nearbystores_rating_app.models import Rating

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
    

    #  Rating
    
    for shop in shops:
        # Get the average rating for each shop
        avg_rating = Rating.objects.filter(shop=shop).aggregate(Avg('rating'))['rating__avg']
        avg_rating = avg_rating if avg_rating is not None else 0
        
        # Add the average rating to each shop object (or use a dictionary to attach ratings)
        shop.avg_rating = round(avg_rating, 1)
    

    #  rating


    context = {
        'form': form,
        'shops': shops,
        'shop_owner_first_name': shop_owner.shop_owner_first_name,
        'shop_owner_last_name': shop_owner.shop_owner_last_name,
        'shop_owner_shop_name': shop_owner.shop_owner_shop_name,
        'shop_owner_village_name': shop_owner.shop_owner_village_name,
        'shop_owner_id': shop_owner_id,
        # 'shop_owner_shop_rating': avg_rating,
    }
    
    return render(request, 'shopownernearbystores.html', context)

def selected_shop_owner_products_data(request, n_shop_owner_id):
    shop_user_name = get_object_or_404(shop_owner_registration_model, pk=n_shop_owner_id)
    shop_owner_products = shop_owner_add_items.objects.filter(shop_user_name=shop_user_name)

    context = {
        'shop_owner_first_name': shop_user_name.shop_owner_first_name,
        'shop_owner_last_name': shop_user_name.shop_owner_last_name,
        'shop_owner_shop_name': shop_user_name.shop_owner_shop_name,
        'shop_owner_id': n_shop_owner_id,
        'shop_owner_products': shop_owner_products,
        'shop_owner_street_address': shop_user_name.shop_owner_street_address,
        'shop_owner_village_name': shop_user_name.shop_owner_village_name,
        'shop_owner_mandal_name': shop_user_name.shop_owner_mandal_name,
        'shop_owner_city_name': shop_user_name.shop_owner_city_name,
        'shop_owner_state_name': shop_user_name.shop_owner_state_name,
        'shop_owner_pincode': shop_user_name.shop_owner_pincode,
    }

    return render(request, 'shop_owner_nearby_shop_products.html', context)
