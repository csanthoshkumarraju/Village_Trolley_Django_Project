from django.shortcuts import render,get_object_or_404,redirect
from shop_owner_registration_app.models import shop_owner_registration_model
from shop_owner_add_items_app.models import shop_owner_add_items
from .models import SearchHistory,ProductTransaction
from django.contrib import messages

def shop_owner_billing(request,shop_owner_id):
    shop_user_name = get_object_or_404(shop_owner_registration_model, pk=shop_owner_id)
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
    
    query = request.GET.get('q', '')
    products = []

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
        SearchHistory.objects.filter(shop_owner_id=shop_owner_id).delete()
        # Process form data to save transactions
        for product_id, quantity, price, total_amount in zip(
                request.POST.getlist('product_ids'),
                request.POST.getlist('quantities'),
                request.POST.getlist('prices'),
                request.POST.getlist('total_amounts')
        ):
            ProductTransaction.objects.create(
                shop_owner=shop_user_name,
                product_id=product_id,
                product_name=shop_owner_add_items.objects.get(id=product_id).product_name,
                quantity=quantity,
                price=price,
                total_amount=total_amount
            )

        messages.success(request, 'Products have been billed successfully. Thank you, @Village Trolley. Please add the products for the next bill.')
        
        return redirect('shop_owner_billing',shop_owner_id)
    context = { 'shop_owner_first_name': shop_user_name.shop_owner_first_name,
                'shop_owner_last_name': shop_user_name.shop_owner_last_name,
                'shop_owner_shop_name': shop_user_name.shop_owner_shop_name,
                'shop_owner_id': shop_owner_id,
                'products': products,
                
                }
    return render(request,'billingform.html',context)
