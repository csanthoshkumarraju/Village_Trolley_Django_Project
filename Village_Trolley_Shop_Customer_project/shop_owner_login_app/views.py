from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from .forms import shop_owner_login_form
from shop_owner_registration_app.models import shop_owner_registration_model
from django.http import HttpResponse
# Create your views here.

def shop_owner_login_view(request):
    if request.method == "POST":
        form = shop_owner_login_form(request.POST)
        if form.is_valid():
            phone_number = form.cleaned_data['phone_number']
            password = form.cleaned_data['password']
            
            try:
                shop_owner = shop_owner_registration_model.objects.get(shop_owner_phone_number=phone_number)
                if shop_owner.shop_owner_password == password:  # Corrected field name
                    request.session['shop_owner_id'] = shop_owner.id  # Storing shop_owner id in session
                    # return HttpResponse('Login successful!')
                    return redirect('shop_owner_add_items',shop_owner_id=shop_owner.id) 
                else:
                    form.add_error(None, "Incorrect password")
            except shop_owner_registration_model.DoesNotExist:
                form.add_error(None, "Shop owner with this phone number does not exist")
    else:
        form = shop_owner_login_form()

    return render(request, 'login.html', {'form': form})
