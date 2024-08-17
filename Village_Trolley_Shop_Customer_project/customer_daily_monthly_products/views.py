from django.shortcuts import render, redirect, get_object_or_404
import datetime
from django.db.models import Sum
from shop_owner_billing_app.models import CustomerPurchase


from customer_registration_app.models import customer_registration_model  

def customer_daily_monthly_purchasing_data(request):
    if 'customer_id' not in request.session:
        return redirect('customer_login')
    
    customer_id = request.session['customer_id']
    customer = get_object_or_404(customer_registration_model, pk=customer_id)
    
    # Ensure phone number is treated as an integer
    customer_phone_number = int(customer.customer_phone_number)

    # Get selected date and month from GET parameters
    daily_date_str = request.GET.get('c_daily_date', datetime.date.today().strftime('%d-%m-%Y'))
    monthly_date_str = request.GET.get('c_monthly_date', datetime.date.today().strftime('%m-%Y'))
    
    # Parse daily date
    try:
        daily_search_date = datetime.datetime.strptime(daily_date_str, '%d-%m-%Y').date()
    except ValueError:
        daily_search_date = datetime.date.today()
    
    # Parse monthly date
    try:
        monthly_search_date = datetime.datetime.strptime(monthly_date_str, '%m-%Y').date()
        start_date = monthly_search_date.replace(day=1)
        next_month = start_date.replace(day=28) + datetime.timedelta(days=4)
        end_date = next_month - datetime.timedelta(days=next_month.day)
    except ValueError:
        monthly_search_date = datetime.date.today()
        start_date = monthly_search_date.replace(day=1)
        next_month = start_date.replace(day=28) + datetime.timedelta(days=4)
        end_date = next_month - datetime.timedelta(days=next_month.day)
    
    # Filter customer purchases for the selected date
    daily_purchases = CustomerPurchase.objects.filter(
        phone_number=customer_phone_number,
        submission_date__date=daily_search_date
    )
    
    # Filter customer purchases for the selected month
    monthly_purchases = CustomerPurchase.objects.filter(
        phone_number=customer_phone_number,
        submission_date__date__range=[start_date, end_date]
    )
    
    # Calculate total amounts
    daily_total_amount = daily_purchases.aggregate(total_amount=Sum('total_amount'))['total_amount'] or 0
    monthly_total_amount = monthly_purchases.aggregate(total_amount=Sum('total_amount'))['total_amount'] or 0
    
    formatted_daily_date = daily_search_date.strftime('%d-%m-%Y')
    formatted_monthly_date = monthly_search_date.strftime('%m-%Y')

    context = {
        'customer_first_name': customer.customer_first_name,
        'customer_last_name': customer.customer_last_name,
        'c_daily_selected_date': formatted_daily_date,
        'c_monthly_selected_date': formatted_monthly_date,
        'daily_total_amount': daily_total_amount,
        'monthly_total_amount': monthly_total_amount,
        'daily_transactions': daily_purchases,
        'monthly_transactions': monthly_purchases,
    }

    return render(request, 'customerdailymonthlypurchasingdata.html', context)


