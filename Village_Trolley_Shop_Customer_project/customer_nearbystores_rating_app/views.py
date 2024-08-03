from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from .models import shop_owner_registration_model, Rating
from .forms import ShopSearchForm,RatingForm
from customer_registration_app.models import customer_registration_model  


# def shop_rating_view(request):
#     # Ensure customer_id is in session
#     if 'customer_id' not in request.session:
#         return redirect('customer_login')

#     customer_id = request.session['customer_id']
#     customer = get_object_or_404(customer_registration_model, pk=customer_id)

#     if request.method == 'POST':
#         form = ShopAndRatingForm(request.POST)
#         if form.is_valid():
#             shop = form.cleaned_data.get('shop')
#             rating = form.cleaned_data['rating']
#             if shop:
#                 # Get or create the customer instance
#                 customer_instance = get_object_or_404(customer_registration_model, pk=customer_id)
                
#                 # Create or update the rating for the shop using customer_id
#                 Rating.objects.update_or_create(
#                     shop=shop,
#                     user=customer_instance,
#                     defaults={'rating': rating}
#                 )
#                 # return redirect('success')
#                 messages.success(request, 'Rating submission successful.')
#                 return render(request, 'customer_nearbystores_rating_app.html')
#                 # return HttpResponse('Rating submission successful.')
#     else:
#         form = ShopAndRatingForm()

#     context = {
#         'form': form,
#         'customer_first_name': customer.customer_first_name,
#         'customer_last_name': customer.customer_last_name,
#     }

#     return render(request, 'customer_nearbystores_rating_app.html', context)

# def shop_rating_view(request):
#     if 'customer_id' not in request.session:
#         return redirect('customer_login')

#     customer_id = request.session['customer_id']
#     customer = get_object_or_404(customer_registration_model, pk=customer_id)

#     search_form = ShopSearchForm()
#     rating_form = RatingForm()
#     shop = None  
#     if request.method == 'POST':
#         if 'search' in request.POST:
#             # Handle shop search
#             search_form = ShopSearchForm(request.POST)
#             if search_form.is_valid():
#                 shop_name = search_form.cleaned_data['shop_name']
#                 try:
#                     shop = shop_owner_registration_model.objects.get(shop_owner_shop_name__iexact=shop_name)
#                     messages.success(request, 'Shop found. You can now submit your rating.')
#                 except shop_owner_registration_model.DoesNotExist:
#                     messages.error(request, 'Shop not found. Please try again.')
#         elif 'submit_rating' in request.POST:
#             # Handle rating submission
#             if shop:  # Ensure shop is found before processing rating
#                 rating_form = RatingForm(request.POST)
#                 if rating_form.is_valid():
#                     rating = rating_form.cleaned_data['rating']
#                     customer_instance = get_object_or_404(customer_registration_model, pk=customer_id)
                    
#                     Rating.objects.update_or_create(
#                         shop=shop,
#                         user=customer_instance,
#                         defaults={'rating': rating}
#                     )
#                     messages.success(request, 'Rating submission successful.')
#                     HttpResponse('success')
#                 else:
#                     messages.error(request, 'Invalid rating. Please try again.')
#             else:
#                 messages.error(request, 'No shop selected for rating.')

#     context = {
#         'search_form': search_form,
#         'rating_form': rating_form if shop else None,
#         'customer_first_name': customer.customer_first_name,
#         'customer_last_name': customer.customer_last_name,
#     }

#     return render(request, 'customer_nearbystores_rating_app.html', context)

def shop_rating_view(request):
    if 'customer_id' not in request.session:
        # print("Customer ID not in session. Redirecting to login.")
        return redirect('customer_login')

    customer_id = request.session['customer_id']
    customer = get_object_or_404(customer_registration_model, pk=customer_id)
    # print(f"Customer fetched: {customer}")

    search_form = ShopSearchForm()
    rating_form = RatingForm()
    shop = None

    if request.method == 'POST':
        if 'search' in request.POST:
            # Handle shop search
            search_form = ShopSearchForm(request.POST)
            if search_form.is_valid():
                shop_name = search_form.cleaned_data['shop_name']
                # print(f"Searching for shop with name: {shop_name}")
                try:
                    shop = shop_owner_registration_model.objects.get(shop_owner_shop_name__iexact=shop_name)
                    # print(f"Shop found: {shop}")
                    # Store the shop ID in session
                    request.session['shop_id'] = shop.id
                    messages.success(request, 'Shop found. You can now submit your rating.')
                except shop_owner_registration_model.DoesNotExist:
                    # print("Shop not found.")
                    messages.error(request, 'Shop not found. Please try again.')
            else:
                # print(f"Search form errors: {search_form.errors}")
                pass

        elif 'submit_rating' in request.POST:
            # Retrieve the shop from session
            shop_id = request.session.get('shop_id')
            if shop_id:
                shop = get_object_or_404(shop_owner_registration_model, pk=shop_id)
                rating_form = RatingForm(request.POST)
                if rating_form.is_valid():
                    rating = rating_form.cleaned_data['rating']
                    # print(f"Rating to be submitted: {rating}")
                    customer_instance = get_object_or_404(customer_registration_model, pk=customer_id)
                    
                    Rating.objects.update_or_create(
                        shop=shop,
                        user=customer_instance,
                        defaults={'rating': rating}
                    )
                    # print("Rating submitted successfully.")
                    messages.success(request, 'Rating submission successful.')
                    # Optionally clear the shop ID from session after successful submission
                    del request.session['shop_id']
                else:
                    # print(f"Rating form errors: {rating_form.errors}")
                    messages.error(request, 'Invalid rating. Please try again.')
            else:
                # print("No shop selected for rating.")
                messages.error(request, 'No shop selected for rating.')

    context = {
        'search_form': search_form,
        'rating_form': rating_form if shop else None,
        'customer_first_name': customer.customer_first_name,
        'customer_last_name': customer.customer_last_name,
    }

    return render(request, 'customer_nearbystores_rating_app.html', context)
