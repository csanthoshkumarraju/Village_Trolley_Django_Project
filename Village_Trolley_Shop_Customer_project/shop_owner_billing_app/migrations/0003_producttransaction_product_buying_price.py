# Generated by Django 5.0.7 on 2024-08-11 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_owner_billing_app', '0002_producttransaction'),
    ]

    operations = [
        migrations.AddField(
            model_name='producttransaction',
            name='product_buying_price',
            field=models.IntegerField(null=True),
        ),
    ]
