from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .models import shop_owner_registration_model,shop_owner_add_items
from .forms import shop_owner_add_items_form

# Create your views here.
# def add_items_for_shop_owner(request, shop_owner_id):
#     shop_user_name = get_object_or_404(shop_owner_registration_model, pk=shop_owner_id)
#     shop_add_items, created = shop_owner_add_items.objects.get_or_create(shop_user_name=shop_user_name)
    
#     if request.method == 'POST':
#         form = shop_owner_add_items_form(request.POST, instance=shop_add_items)
#         if form.is_valid():
#             form.save()
#             return HttpResponse('Items added successfully')
#         else:
#             print(form.errors)
#     else:
#         form = shop_owner_add_items_form(instance=shop_add_items)
#     context = {
#         'form': form,
#         'shop_owner_first_name': shop_user_name.shop_owner_first_name,
#         'shop_owner_last_name': shop_user_name.shop_owner_last_name,
#         'shop_owner_shop_name': shop_user_name.shop_owner_shop_name,
#     }
    
#     return render(request, 'additems.html', context)


# def add_items_for_shop_owner(request, shop_owner_id):
#     shop_user_name = get_object_or_404(shop_owner_registration_model, pk=shop_owner_id)
    
#     if request.method == 'POST':
#         # Retrieve the product details from the POST request
#         product_names = request.POST.getlist('product_name[]')
#         buying_prices = request.POST.getlist('product_buying_price[]')
#         selling_prices = request.POST.getlist('product_selling_price[]')
#         quantities = request.POST.getlist('product_quantity[]')
#         storage_places = request.POST.getlist('product_storage_place[]')
        
#         # Check if lists are of the same length
#         if len(product_names) == len(buying_prices) == len(selling_prices) == len(quantities) == len(storage_places):
#             # Iterate through each product entry and save them
#             for i in range(len(product_names)):
#                 shop_owner_add_items.objects.create(
#                     shop_user_name=shop_user_name,
#                     product_name=product_names[i],
#                     product_buying_price=buying_prices[i],
#                     product_selling_price=selling_prices[i],
#                     product_qunatity=quantities[i],
#                     product_storage_place=storage_places[i]
#                 )
#             return HttpResponse('Items added successfully')
#         else:
#             # Handle the error when lists are not of the same length
#             return HttpResponse('Error: Mismatched input lengths', status=400)

#     else:
#         # Initialize an empty form since the model instance is not used for form initialization here
#         form = shop_owner_add_items_form()
    
#     context = {
#         'form': form,
#         'shop_owner_first_name': shop_user_name.shop_owner_first_name,
#         'shop_owner_last_name': shop_user_name.shop_owner_last_name,
#         'shop_owner_shop_name': shop_user_name.shop_owner_shop_name,
#         'shop_owner_id': shop_owner_id,
#     }
    
#     return render(request, 'additems.html', context)

# def add_items_for_shop_owner(request, shop_owner_id):
#     shop_user_name = get_object_or_404(shop_owner_registration_model, pk=shop_owner_id)

#     if request.method == 'POST':
#         # Retrieve the product details from the POST request
#         product_names = request.POST.getlist('product_name[]')
#         buying_prices = request.POST.getlist('product_buying_price[]')
#         selling_prices = request.POST.getlist('product_selling_price[]')
#         quantities = request.POST.getlist('product_quantity[]')
#         storage_places = request.POST.getlist('product_storage_place[]')

#         # Check if lists are of the same length
#         if len(product_names) == len(buying_prices) == len(selling_prices) == len(quantities) == len(storage_places):
#             # Create a list to hold form errors
#             form_errors = []

#             # Iterate through each product entry and validate
#             for i in range(len(product_names)):
#                 form_data = {
#                     'product_name': product_names[i],
#                     'product_buying_price': buying_prices[i],
#                     'product_selling_price': selling_prices[i],
#                     'product_qunatity': quantities[i],
#                     'product_storage_place': storage_places[i]
#                 }
#                 form = shop_owner_add_items_form(data=form_data)
               
#                 if form.is_valid():
#                     # Save the valid form data
#                     shop_owner_add_items.objects.create(
#                         shop_user_name=shop_user_name,
#                         **form.cleaned_data
#                     )
#                 else:
#                     form_errors.append(form.errors)

#             if form_errors:
#                 # Return the form errors to the template
#                 context = {
#                     'form_errors': form_errors,
#                     'shop_owner_first_name': shop_user_name.shop_owner_first_name,
#                     'shop_owner_last_name': shop_user_name.shop_owner_last_name,
#                     'shop_owner_shop_name': shop_user_name.shop_owner_shop_name,
#                     'shop_owner_id': shop_owner_id,
#                 }
#                 return render(request, 'additems.html', context)
#             else:
#                 return HttpResponse('Items added successfully')
#         else:
#             # Handle the error when lists are not of the same length
#             return HttpResponse('Error: Mismatched input lengths', status=400)
#     else:
#         # Initialize an empty form since the model instance is not used for form initialization here
#         form = shop_owner_add_items_form()

#     context = {
#         'form': form,
#         'shop_owner_first_name': shop_user_name.shop_owner_first_name,
#         'shop_owner_last_name': shop_user_name.shop_owner_last_name,
#         'shop_owner_shop_name': shop_user_name.shop_owner_shop_name,
#         'shop_owner_id': shop_owner_id,
#     }

#     return render(request, 'additems.html', context)

def add_items_for_shop_owner(request, shop_owner_id):
    shop_user_name = get_object_or_404(shop_owner_registration_model, pk=shop_owner_id)

    if request.method == 'POST':
        product_names = request.POST.getlist('product_name[]')
        buying_prices = request.POST.getlist('product_buying_price[]')
        selling_prices = request.POST.getlist('product_selling_price[]')
        quantities = request.POST.getlist('product_quantity[]')
        storage_places = request.POST.getlist('product_storage_place[]')

        if len(product_names) == len(buying_prices) == len(selling_prices) == len(quantities) == len(storage_places):
            form_errors = {}

            for i in range(len(product_names)):
                form_data = {
                    'product_name': product_names[i],
                    'product_buying_price': buying_prices[i],
                    'product_selling_price': selling_prices[i],
                    'product_qunatity': quantities[i],
                    'product_storage_place': storage_places[i]
                }
                form = shop_owner_add_items_form(data=form_data)
                
                if form.is_valid():
                    shop_owner_add_items.objects.create(
                        shop_user_name=shop_user_name,
                        **form.cleaned_data
                    )
                else:
                    for field, error in form.errors.items():
                        if field not in form_errors:
                            form_errors[field] = []
                        form_errors[field].extend(error)

            if form_errors:
                context = {
                    'form_errors': form_errors,
                    'shop_owner_first_name': shop_user_name.shop_owner_first_name,
                    'shop_owner_last_name': shop_user_name.shop_owner_last_name,
                    'shop_owner_shop_name': shop_user_name.shop_owner_shop_name,
                    'shop_owner_id': shop_owner_id,
                }
                return render(request, 'additems.html', context)
            else:
                # return HttpResponse('Items added successfully')
                return redirect('shop_owner_products_data',shop_owner_id)
        else:
            return HttpResponse('Error: Mismatched input lengths', status=400)
    else:
        form = shop_owner_add_items_form()

    context = {
        'form': form,
        'shop_owner_first_name': shop_user_name.shop_owner_first_name,
        'shop_owner_last_name': shop_user_name.shop_owner_last_name,
        'shop_owner_shop_name': shop_user_name.shop_owner_shop_name,
        'shop_owner_id': shop_owner_id,
    }

    return render(request, 'additems.html', context)