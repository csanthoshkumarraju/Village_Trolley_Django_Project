from django.shortcuts import render
from shop_owner_registration_app.models import shop_owner_registration_model
# Create your views here.

def shop_user_name(request):
    shop_owner_name_instance = shop_owner_registration_model.objects.first()
    if shop_owner_name_instance:
        print(f"Found instance: {shop_owner_name_instance.shop_owner_first_name}")
    else:
        print("No instance found")
    context = {
        'shop_owner_name_instance': shop_owner_name_instance,
    }
    return render(request, 'nav.html', context)

