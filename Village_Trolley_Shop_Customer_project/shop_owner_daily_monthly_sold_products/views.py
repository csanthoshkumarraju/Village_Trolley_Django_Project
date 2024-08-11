from django.shortcuts import render,get_object_or_404
from shop_owner_registration_app.models import shop_owner_registration_model
from shop_owner_billing_app.models import ProductTransaction
import datetime
from django.db.models import Sum
# Create your views here.

def daily_monthly_sold_products(request, shop_owner_id):
    shop_user_name = get_object_or_404(shop_owner_registration_model, pk=shop_owner_id)
    # date_str = request.GET.get('date', datetime.date.today().strftime('%d-%m-%Y'))
    
    # try:
    #     # Parse the input date string
    #     search_date = datetime.datetime.strptime(date_str, '%d-%m-%Y').date()
    # except ValueError:
    #     search_date = datetime.date.today()
    
    # # Query the ProductTransaction model
    # transactions = ProductTransaction.objects.filter(
    #     shop_owner=shop_owner_id,
    #     search_date__date=search_date
    # )

    daily_date_str = request.GET.get('daily_date', datetime.date.today().strftime('%d-%m-%Y'))
    monthly_date_str = request.GET.get('monthly_date', datetime.date.today().strftime('%m-%Y'))

    try:
        daily_search_date = datetime.datetime.strptime(daily_date_str, '%d-%m-%Y').date()
    except ValueError:
        daily_search_date = datetime.date.today()

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
    
    daily_transactions = ProductTransaction.objects.filter(
        shop_owner=shop_owner_id,
        search_date__date=daily_search_date
    )
    
    # Query for monthly transactions
    monthly_transactions = ProductTransaction.objects.filter(
        shop_owner=shop_owner_id,
        search_date__date__range=[start_date, end_date]
    )

    # daily_total_amount = daily_transactions.aggregate(total_amount=Sum('price'))['total_amount'] or 0
    # monthly_total_amount = monthly_transactions.aggregate(total_amount=Sum('price'))['total_amount'] or 0
    daily_total_amount = daily_transactions.aggregate(total_amount=Sum('total_amount'))['total_amount'] or 0
    monthly_total_amount = monthly_transactions.aggregate(total_amount=Sum('total_amount'))['total_amount'] or 0


    context = {
        'shop_owner': shop_user_name,
        'shop_owner_id': shop_owner_id,
        'shop_owner_first_name': shop_user_name.shop_owner_first_name,
        'shop_owner_last_name': shop_user_name.shop_owner_last_name,
        'shop_owner_shop_name': shop_user_name.shop_owner_shop_name,
        'daily_transactions': daily_transactions,
        'monthly_transactions': monthly_transactions,
        'daily_selected_date': daily_search_date.strftime('%d-%m-%Y'),
        'monthly_selected_date': monthly_search_date.strftime('%m-%Y'),
        'daily_total_amount': daily_total_amount,
        'monthly_total_amount': monthly_total_amount,
    }
    return render(request, 'dailymonthlydata.html',context)
