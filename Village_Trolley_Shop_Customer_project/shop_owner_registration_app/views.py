from django.shortcuts import render,redirect
from django.http import HttpResponse
# Create your views here.

from django.contrib import messages  
from .forms import shop_owner_registration_form
from .models import shop_owner_registration_model

def shop_owner_registration(request):
    if request.method == 'POST':
        form = shop_owner_registration_form(request.POST)
        if form.is_valid():
            # Process the form data if it is valid
            shop_owner_shop_name = form.cleaned_data['shop_owner_shop_name']
            # Check if a student with the same name already exists
            if shop_owner_registration_model.objects.filter(shop_owner_shop_name=shop_owner_shop_name).exists():
                messages.error(request, f'A shop with this name  already exists.')
            
            shop_owner_mail_id = form.cleaned_data['shop_owner_mail_id']
            if shop_owner_registration_model.objects.filter(shop_owner_mail_id=shop_owner_mail_id).exists():
                messages.error(request, f'This mail already exists.')
            
            shop_owner_phone_number = form.cleaned_data['shop_owner_phone_number']
            if shop_owner_registration_model.objects.filter(shop_owner_phone_number=shop_owner_phone_number).exists():
                messages.error(request, f'This phone number already exists.')
            else:
                form.save()
                # Redirect or perform other actions after successful form submission
                # return redirect('login')  # Redirect to clear form data on reload
                # print(f"Shop name: {shop_owner_shop_name}")
                return HttpResponse('Registration successful!')

        else:
            # Handle form errors if any
            messages.error(request, 'Please correct the errors below.')
    else:
        form = shop_owner_registration_form()


    return render(request,'register.html',{'form': form})