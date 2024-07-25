from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .forms import PasswordUpdateForm
from shop_owner_registration_app.models import shop_owner_registration_model

def update_password(request):
    if request.method == 'POST':
        form = PasswordUpdateForm(request.POST)
        if form.is_valid():
            mobile_number = form.cleaned_data['mobile_number']
            password = form.cleaned_data['password']
            confirm_password = form.cleaned_data['confirm_password']

            # Check if shop owner with given mobile number exists
            try:
                shop_owner = shop_owner_registration_model.objects.get(shop_owner_phone_number=mobile_number)
            except shop_owner_registration_model.DoesNotExist:
                form.add_error('mobile_number', "Mobile number is not registered.")
                return render(request, 'resetpassword.html', {'form': form})

            # Update the password
            if password == confirm_password:
                shop_owner.shop_owner_password = password
                shop_owner.save()

                # Pass success message to template
                success_message = "Password successfully updated. You can now login."
                return render(request, 'resetpassword.html', {'form': form, 'success_message': success_message})
            else:
                form.add_error('confirm_password', "Passwords do not match.")
    else:
        form = PasswordUpdateForm()

    return render(request, 'resetpassword.html', {'form': form})