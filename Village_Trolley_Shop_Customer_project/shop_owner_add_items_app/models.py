from django.db import models
from shop_owner_registration_app.models import shop_owner_registration_model


# Create your models here.
class shop_owner_add_items(models.Model):
    #  shop_owner_name = models.OneToOneField(shop_owner_registration_model, primary_key=True, on_delete=models.CASCADE)
     shop_user_name = models.ForeignKey(shop_owner_registration_model, on_delete=models.CASCADE)
     product_name = models.CharField(max_length=500,null=True)
     product_buying_price = models.IntegerField(null=True)
     product_selling_price = models.IntegerField(null=True)
     product_qunatity = models.IntegerField(null=True)
     product_storage_place = models.CharField(max_length=50,null=True)

     def __str__(self):
        return {self.product_name}


