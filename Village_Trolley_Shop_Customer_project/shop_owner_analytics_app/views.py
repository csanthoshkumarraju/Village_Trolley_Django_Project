from django.shortcuts import render,get_object_or_404
from shop_owner_registration_app.models import shop_owner_registration_model
from shop_owner_billing_app.models import ProductTransaction
from django.utils.timezone import now
from django.db.models import Sum
from datetime import date


def shop_owner_analytics(request,shop_owner_id):
    shop_user_name = get_object_or_404(shop_owner_registration_model, pk=shop_owner_id)
    
    today = now().date()
    start_of_month = today.replace(day=1)
    start_of_year = today.replace(month=1, day=1)

    today_transactions = ProductTransaction.objects.filter(
        shop_owner=shop_user_name,
        search_date__date=today
    )

    monthly_transactions = ProductTransaction.objects.filter(
        shop_owner=shop_user_name,
        search_date__date__gte=start_of_month
    )



    yearly_transactions = ProductTransaction.objects.filter(
        shop_owner=shop_user_name,
        search_date__date__gte=start_of_year
    )

    total_sold_today = today_transactions.aggregate(total_amount=Sum('total_amount'))['total_amount'] or 0
    total_quantity_today = today_transactions.aggregate(total_quantity=Sum('quantity'))['total_quantity'] or 0
    total_buying_price_today = today_transactions.aggregate(total_buying_price=Sum('product_buying_price'))['total_buying_price'] or 0
    profit_or_loss_today = total_sold_today - total_buying_price_today

    total_sold_month = monthly_transactions.aggregate(total_amount=Sum('total_amount'))['total_amount'] or 0
    total_quantity_month = monthly_transactions.aggregate(total_quantity=Sum('quantity'))['total_quantity'] or 0
    total_buying_price_month = monthly_transactions.aggregate(total_buying_price=Sum('product_buying_price'))['total_buying_price'] or 0
    profit_or_loss_month = total_sold_month - total_buying_price_month

    total_sold_year = yearly_transactions.aggregate(total_amount=Sum('total_amount'))['total_amount'] or 0
    total_quantity_year = yearly_transactions.aggregate(total_quantity=Sum('quantity'))['total_quantity'] or 0
    total_buying_price_year = yearly_transactions.aggregate(total_buying_price=Sum('product_buying_price'))['total_buying_price'] or 0
    profit_or_loss_year = total_sold_year - total_buying_price_year

    total_investment = ProductTransaction.objects.filter(shop_owner=shop_user_name).aggregate(total_investment=Sum('product_buying_price'))['total_investment'] or 0
    total_return = ProductTransaction.objects.filter(shop_owner=shop_user_name).aggregate(total_return=Sum('total_amount'))['total_return'] or 0
    total_profit = total_return - total_investment
    total_loss = total_return - total_investment

    product_quantities = ProductTransaction.objects.filter(shop_owner=shop_user_name).values('product_name').annotate(
    total_quantity_sold=Sum('quantity')
    ).order_by('-total_quantity_sold')
    most_selling_products = product_quantities[:5]
    product_quantities_sorted_ascending = product_quantities.order_by('total_quantity_sold')
    least_selling_products = product_quantities_sorted_ascending[:5] if len(product_quantities_sorted_ascending) >= 5 else []
    most_selling_products_list = ', '.join(p['product_name'] for p in most_selling_products)
    least_selling_products_list = ', '.join(p['product_name'] for p in least_selling_products)

    context = { 'shop_owner_first_name': shop_user_name.shop_owner_first_name,
                'shop_owner_last_name': shop_user_name.shop_owner_last_name,
                'shop_owner_shop_name': shop_user_name.shop_owner_shop_name,
                'shop_owner_id': shop_owner_id,
                'total_sold_today': total_sold_today,
                'total_quantity_today': total_quantity_today,
                'profit_or_loss_today': profit_or_loss_today,
                'total_sold_month': total_sold_month,
                'total_quantity_month': total_quantity_month,
                'profit_or_loss_month': profit_or_loss_month,
                'total_sold_year': total_sold_year,
                'total_quantity_year': total_quantity_year,
                'profit_or_loss_year': profit_or_loss_year,
                'total_investment': total_investment,
                'total_return': total_return,
                'total_profit': total_profit if total_profit > 0 else 0,
                'total_loss': total_loss if total_loss < 0 else 0,
                'most_selling_products': most_selling_products_list,
                'least_selling_products': least_selling_products_list,
                }
    return render(request,'analytics.html',context)