from django.shortcuts import render,get_object_or_404,redirect
from shop_owner_registration_app.models import shop_owner_registration_model
from shop_owner_add_items_app.models import shop_owner_add_items
from .forms import Customer_ShopSearchForm
from customer_registration_app.models import customer_registration_model
from django.db.models import Avg
from customer_nearbystores_rating_app.models import Rating

# def customer_search_nearby_shops(request):
#     return render(request,'customernearbystores.html')


def customer_search_nearby_shops(request):
    # Check if the customer is logged in
    if 'customer_id' not in request.session:
        return redirect('customer_login')

    customer_id = request.session['customer_id']
    customer = get_object_or_404(customer_registration_model, pk=customer_id)

    # Initialize the search form
    form = Customer_ShopSearchForm(request.GET or None)
    shops = []

    # If the form is valid, filter shops based on the village name
    if form.is_valid():
        village_name = form.cleaned_data.get('village_name')
        if village_name:
            shops = shop_owner_registration_model.objects.filter(shop_owner_village_name__icontains=village_name)


        #  Rating
    
    for shop in shops:
        # Get the average rating for each shop
        avg_rating = Rating.objects.filter(shop=shop).aggregate(Avg('rating'))['rating__avg']
        avg_rating = avg_rating if avg_rating is not None else 0
        
        # Add the average rating to each shop object (or use a dictionary to attach ratings)
        shop.avg_rating = round(avg_rating, 1)
    

    #  rating

    # Prepare the context with both customer details and search results
    context = {
        'form': form,
        'shops': shops,
        'customer_first_name': customer.customer_first_name,
        'customer_last_name': customer.customer_last_name,
        'customer_id': customer_id,
        # 'shop_owner_shop_rating': avg_rating,
    }

    return render(request, 'customernearbystores.html', context)

def customer_selected_shop_owner_products_data(request, shop_owner_id):
    shop_user_name = get_object_or_404(shop_owner_registration_model, pk=shop_owner_id)
    shop_owner_products = shop_owner_add_items.objects.filter(shop_user_name=shop_user_name)

    context = {
        'shop_owner_first_name': shop_user_name.shop_owner_first_name,
        'shop_owner_last_name': shop_user_name.shop_owner_last_name,
        'shop_owner_shop_name': shop_user_name.shop_owner_shop_name,
        'shop_owner_id': shop_owner_id,
        'shop_owner_products': shop_owner_products,
        'shop_owner_street_address': shop_user_name.shop_owner_street_address,
        'shop_owner_village_name': shop_user_name.shop_owner_village_name,
        'shop_owner_mandal_name': shop_user_name.shop_owner_mandal_name,
        'shop_owner_city_name': shop_user_name.shop_owner_city_name,
        'shop_owner_state_name': shop_user_name.shop_owner_state_name,
        'shop_owner_pincode': shop_user_name.shop_owner_pincode,
    }

    return render(request, 'customer_shop_owner_nearby_shop_products.html', context)
