from django.db import models

# Create your models here.
class customer_registration_model(models.Model):
     customer_first_name = models.CharField(max_length=100,null=True)
     customer_last_name  = models.CharField(max_length=150,null=True)
     customer_mail_id = models.EmailField(max_length=254,null=True)
     customer_phone_number =models.IntegerField(null=True,max_length=10)
     customer_password = models.CharField(max_length=50,null=True)
     customer_confirm_password = models.CharField(max_length=50,null=True)

     def __str__(self):
         return self.customer_first_name
     
