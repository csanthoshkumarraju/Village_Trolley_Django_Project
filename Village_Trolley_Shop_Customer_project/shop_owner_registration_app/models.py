from django.db import models

# Create your models here.

class shop_owner_registration_model(models.Model):
    shop_owner_first_name = models.CharField(max_length=250,null=True)
    shop_owner_last_name = models.CharField(max_length=250,null=True)
    shop_owner_shop_name = models.CharField(max_length=250,null=True,unique=True)
    shop_owner_mail_id = models.EmailField(max_length=254,null=True,unique=True)
    shop_owner_phone_number = models.IntegerField(null=True,max_length=10,unique=True)
    shop_owner_street_address = models.CharField(max_length=1500,null=True)
    shop_owner_village_name = models.CharField(max_length=1500,null=True)
    shop_owner_mandal_name = models.CharField(max_length=1500,null=True)
    shop_owner_city_name = models.CharField(max_length=1500,null=True)
    shop_owner_state_name = models.CharField(max_length=1500,null=True)
    shop_owner_pincode = models.IntegerField(max_length=10,null=True)
    shop_owner_password = models.CharField( max_length=50,null=True)
    shop_owner_confirm_password = models.CharField( max_length=50,null=True)

    def __str__(self):
        return self.shop_owner_first_name


