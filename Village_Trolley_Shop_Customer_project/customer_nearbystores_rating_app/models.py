from django.db import models
from shop_owner_registration_app.models import shop_owner_registration_model
from customer_registration_app.models import customer_registration_model

# Create your models here.
class Rating(models.Model):
    shop = models.ForeignKey(shop_owner_registration_model, on_delete=models.CASCADE)
    user = models.ForeignKey(customer_registration_model, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField()

    def __str__(self):
        return f"Rating {self.rating} for {self.shop.shop_owner_shop_name} by {self.user.username}"