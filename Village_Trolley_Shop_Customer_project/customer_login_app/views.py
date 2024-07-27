from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import customer_login_form
from customer_registration_app.models import customer_registration_model

# Create your views here.
def customer_login_fun(request):
    form = customer_login_form()  # Initialize the form variable

    if request.method == 'POST':
        form = customer_login_form(request.POST)  # Reinitialize the form with POST data
        if form.is_valid():
            phone_number = form.cleaned_data['customer_phone_number']
            password = form.cleaned_data['customer_password']

            try:
                customer = customer_registration_model.objects.get(customer_phone_number=phone_number)
                if customer.customer_password == password:
                    request.session['customer_id'] = customer.id
                    return HttpResponse('Login Successful')
                else:
                    form.add_error(None, "Incorrect password")
            except customer_registration_model.DoesNotExist:
                form.add_error(None, "Customer with this phone number does not exist")

    # Render the form with errors or empty form if GET request
    return render(request, 'customerlogin.html', {'form': form})