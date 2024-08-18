# models.py
from django.db import models


from shop_owner_registration_app.models import shop_owner_registration_model
class SearchHistory(models.Model):
    shop_owner_id = models.IntegerField()
    query = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

class ProductTransaction(models.Model):
    shop_owner = models.ForeignKey(shop_owner_registration_model, on_delete=models.CASCADE)  
    product_id = models.IntegerField()
    product_name = models.CharField(max_length=255)
    quantity = models.FloatField()  
    price = models.DecimalField(max_digits=10, decimal_places=2)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    search_date = models.DateTimeField(auto_now_add=True)
    product_buying_price = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return f'{self.product_name} - {self.quantity} KG - {self.total_amount}'
    
class CustomerPurchase(models.Model):
    phone_number = models.CharField(max_length=200,null=True)
    product_name = models.CharField(max_length=255,null=True)
    quantity = models.PositiveIntegerField(null=True)
    total_amount = models.DecimalField(max_digits=100, decimal_places=2,null=True)
    submission_date = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return f"{self.phone_number} - {self.product_name} - {self.quantity}"
    
class PhoneNumberSearchResult(models.Model):
    phone_number = models.CharField(max_length=150)

    def __str__(self):
        return self.phone_number