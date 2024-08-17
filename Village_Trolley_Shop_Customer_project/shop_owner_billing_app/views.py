from django.shortcuts import render,get_object_or_404,redirect
from shop_owner_registration_app.models import shop_owner_registration_model
from shop_owner_add_items_app.models import shop_owner_add_items
from .models import SearchHistory,ProductTransaction,CustomerPurchase,PhoneNumberSearchResult
from django.contrib import messages
from customer_registration_app.models import customer_registration_model
from customer_registration_app.models import customer_registration_model

# def shop_owner_billing(request,shop_owner_id):
#     shop_user_name = get_object_or_404(shop_owner_registration_model, pk=shop_owner_id)
    # query = request.GET.get('q', '')
    # products = []

    # if query:
    #     # Perform the search and update the SearchHistory model
    #     products = shop_owner_add_items.objects.filter(product_name__icontains=query)
    #     SearchHistory.objects.create(shop_owner_id=shop_owner_id, query=query)
    # else:
    #     # Display all search results if there's no new query
    #     search_histories = SearchHistory.objects.filter(shop_owner_id=shop_owner_id).order_by('-created_at')
    #     product_ids = []
    #     for history in search_histories:
    #         products.extend(shop_owner_add_items.objects.filter(product_name__icontains=history.query))
    #         product_ids.extend(shop_owner_add_items.objects.filter(product_name__icontains=history.query).values_list('id', flat=True))
        
    #     # Remove duplicate products
    #     products = list(shop_owner_add_items.objects.filter(id__in=product_ids).distinct())
    
    # query = request.GET.get('q', '')
    # products = []

    # if query:
    #     # Perform the search with the shop owner filter and update the SearchHistory model
    #     products = shop_owner_add_items.objects.filter(
    #         shop_user_name=shop_user_name, 
    #         product_name__icontains=query
    #     )
    #     SearchHistory.objects.create(shop_owner_id=shop_owner_id, query=query)
    # else:
    #     # Display all search results if there's no new query
    #     search_histories = SearchHistory.objects.filter(shop_owner_id=shop_owner_id).order_by('-created_at')
    #     product_ids = []
        
    #     for history in search_histories:
    #         product_ids.extend(
    #             shop_owner_add_items.objects.filter(
    #                 shop_user_name=shop_user_name, 
    #                 product_name__icontains=history.query
    #             ).values_list('id', flat=True)
    #         )
        
    #     # Remove duplicate products
    #     products = list(shop_owner_add_items.objects.filter(
    #         id__in=product_ids, 
    #         shop_user_name=shop_user_name
    #     ).distinct())
    # # product_details = shop_owner_add_items.objects.get(id=product_id)
    # if request.method == 'POST':
    # # Clear existing search history
    #     SearchHistory.objects.filter(shop_owner_id=shop_owner_id).delete()

    #     # Retrieve form data
    #     product_ids = request.POST.getlist('product_ids')
    #     quantities = request.POST.getlist('quantities')
    #     prices = request.POST.getlist('prices')
    #     total_amounts = request.POST.getlist('total_amounts')
    #     total_buying_amounts = request.POST.getlist('total_buying_amounts')  # Changed

    #     # Ensure lists are of the same length
    #     if not all(len(lst) == len(product_ids) for lst in [quantities, prices, total_amounts, total_buying_amounts]):
    #         messages.error(request, 'Form data is incomplete or corrupted.')
    #         return redirect('shop_owner_billing', shop_owner_id=shop_owner_id)

    #     # Process form data and save transactions
    #     for product_id, quantity, price, total_amount, total_buying_amount in zip(
    #             product_ids,
    #             quantities,
    #             prices,
    #             total_amounts,
    #             total_buying_amounts,
    #     ):
    #         try:
    #             product = shop_owner_add_items.objects.get(id=product_id)
    #             ProductTransaction.objects.create(
    #                 shop_owner_id=shop_owner_id,
    #                 product_id=product_id,
    #                 product_name=product.product_name,
    #                 quantity=quantity,
    #                 price=price,
    #                 total_amount=total_amount,
    #                 product_buying_price=total_buying_amount,  # Use total_buying_amount
    #             )
    #         except shop_owner_add_items.DoesNotExist:
    #             messages.error(request, f"Product with ID {product_id} does not exist.")

    #     messages.success(request, 'Products have been billed successfully. Thank you, @Village Trolley. Please add the products for the next bill.')

        
    #     return redirect('shop_owner_billing',shop_owner_id)
    # context = { 'shop_owner_first_name': shop_user_name.shop_owner_first_name,
    #             'shop_owner_last_name': shop_user_name.shop_owner_last_name,
    #             'shop_owner_shop_name': shop_user_name.shop_owner_shop_name,
    #             'shop_owner_id': shop_owner_id,
    #             'products': products,
                
    #             }
    # return render(request,'billingform.html',context)

def shop_owner_billing(request, shop_owner_id):
    shop_user_name = get_object_or_404(shop_owner_registration_model, pk=shop_owner_id)
    query = request.GET.get('q', '')
    products = []
    # latest_entry = PhoneNumberSearchResult.objects.last()
    latest_entry = PhoneNumberSearchResult.objects.first()
    phone_number_from_db = latest_entry.phone_number if latest_entry else None
    customer_first_name = None
    customer_last_name = None
    customer = customer_registration_model.objects.filter(customer_phone_number=phone_number_from_db).first()
    if customer:
        customer_first_name = customer.customer_first_name
        customer_last_name = customer.customer_last_name
    else:
        pass
    if query:
        # Perform the search with the shop owner filter and update the SearchHistory model
        products = shop_owner_add_items.objects.filter(
            shop_user_name=shop_user_name, 
            product_name__icontains=query
        )
        SearchHistory.objects.create(shop_owner_id=shop_owner_id, query=query)
    else:
        # Display all search results if there's no new query
        search_histories = SearchHistory.objects.filter(shop_owner_id=shop_owner_id).order_by('-created_at')
        product_ids = []

        for history in search_histories:
            product_ids.extend(
                shop_owner_add_items.objects.filter(
                    shop_user_name=shop_user_name, 
                    product_name__icontains=history.query
                ).values_list('id', flat=True)
            )

        # Remove duplicate products
        products = list(shop_owner_add_items.objects.filter(
            id__in=product_ids, 
            shop_user_name=shop_user_name
        ).distinct())

    if request.method == 'POST':
        # Clear existing search history
        SearchHistory.objects.filter(shop_owner_id=shop_owner_id).delete()

        # Retrieve form data
        product_ids = request.POST.getlist('product_ids')
        quantities = request.POST.getlist('quantities')
        prices = request.POST.getlist('prices')
        total_amounts = request.POST.getlist('total_amounts')
        total_buying_amounts = request.POST.getlist('total_buying_amounts')

        # Ensure lists are of the same length
        if not all(len(lst) == len(product_ids) for lst in [quantities, prices, total_amounts, total_buying_amounts]):
            messages.error(request, 'Form data is incomplete or corrupted.')
            return redirect('shop_owner_billing', shop_owner_id=shop_owner_id)

        # Process form data and save transactions
        for product_id, quantity, price, total_amount, total_buying_amount in zip(
                product_ids,
                quantities,
                prices,
                total_amounts,
                total_buying_amounts,
        ):
            try:
                product = shop_owner_add_items.objects.get(id=product_id)

                # Update the product quantity
                if product.product_qunatity >= int(quantity):
                    product.product_qunatity -= int(quantity)
                    product.save()

                    # Create transaction record
                    ProductTransaction.objects.create(
                        shop_owner_id=shop_owner_id,
                        product_id=product_id,
                        product_name=product.product_name,
                        quantity=quantity,
                        price=price,
                        total_amount=total_amount,
                        product_buying_price=total_buying_amount,
                    )
                    
                    # print(f"Phone Number being saved: {phone_number_from_db} (Type: {type(phone_number_from_db)})")
                    PhoneNumberSearchResult.objects.all().delete()
                    CustomerPurchase.objects.create(
                        phone_number=phone_number_from_db,
                        product_name=product.product_name,
                        quantity=quantity,
                        total_amount=total_amount,
                    )
                else:
                    messages.error(request, f"Not enough stock for product {product.product_name}. All other products have been billed except {product.product_name}. ")
                    
            except shop_owner_add_items.DoesNotExist:
                messages.error(request, f"Product with ID {product_id} does not exist.")

        messages.success(request, 'Products have been billed successfully. Thank you, @Village Trolley. Please add the products for the next bill.')

        return redirect('shop_owner_billing', shop_owner_id=shop_owner_id)

  
    phone_number = request.GET.get('phone_number', '')
    if phone_number:
        if not phone_number.isdigit():
            phone_number_value = 'Invalid phone number format'
        else:
            try:
                phone_number_value = phone_number        
                PhoneNumberSearchResult.objects.all().delete()
                PhoneNumberSearchResult.objects.create(phone_number=phone_number)
                
            except customer_registration_model.DoesNotExist:
                phone_number_value = 'Phone number not registered'
                
                PhoneNumberSearchResult.objects.all().delete()
                PhoneNumberSearchResult.objects.create(phone_number=phone_number)
    else:
        phone_number_value = ''

    


    context = {
        'shop_owner_first_name': shop_user_name.shop_owner_first_name,
        'shop_owner_last_name': shop_user_name.shop_owner_last_name,
        'shop_owner_shop_name': shop_user_name.shop_owner_shop_name,
        'shop_owner_id': shop_owner_id,
        'products': products,
        'phone_number_value': phone_number_value,
        'phone_number_from_db': phone_number_from_db,
        'customer_first_name': customer_first_name,
        'customer_last_name': customer_last_name,
    }
    return render(request, 'billingform.html', context)
