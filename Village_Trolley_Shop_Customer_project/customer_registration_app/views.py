from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages 
from .forms import customer_registartion_form
from .models import customer_registration_model

# Create your views here.
def customer_registartion_fun(request):
    if request.method == 'POST':
        form = customer_registartion_form(request.POST)
        
        if form.is_valid():
            customer_mail_id = form.cleaned_data['customer_mail_id']
            customer_phone_number = form.cleaned_data['customer_phone_number']
            
            if customer_registration_model.objects.filter(customer_mail_id=customer_mail_id).exists():
                messages.error(request, 'This email is already registered')
            elif customer_registration_model.objects.filter(customer_phone_number=customer_phone_number).exists():
                messages.error(request, 'This phone number is already registered')
            else:
                form.save()
                return redirect('customer_login_fun')
                # return HttpResponse('Registration successful!')
        else:
            # print('Form errors are :- ',form.errors)
            messages.error(request, 'Password and confirm passwords  do not match.')
    else:
        form = customer_registartion_form()
    
    return render(request, 'customerregister.html', {'form': form})