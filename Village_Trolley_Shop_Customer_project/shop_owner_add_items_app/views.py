from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .models import shop_owner_registration_model,shop_owner_add_items
from .forms import shop_owner_add_items_form

# Create your views here.
def add_items_for_shop_owner(request, shop_owner_id):
    shop_user_name = get_object_or_404(shop_owner_registration_model, pk=shop_owner_id)
    shop_add_items, created = shop_owner_add_items.objects.get_or_create(shop_user_name=shop_user_name)
    
    if request.method == 'POST':
        form = shop_owner_add_items_form(request.POST, instance=shop_add_items)
        if form.is_valid():
            form.save()
            return HttpResponse('Items added successfully')
        else:
            print(form.errors)
    else:
        form = shop_owner_add_items_form(instance=shop_add_items)
    context = {
        'form': form,
        'shop_owner_first_name': shop_user_name.shop_owner_first_name,
        'shop_owner_last_name': shop_user_name.shop_owner_last_name,
        'shop_owner_shop_name': shop_user_name.shop_owner_shop_name,
    }
    
    return render(request, 'additems.html', context)