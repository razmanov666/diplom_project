# Generated by Django 4.1 on 2022-08-27 13:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_hotel', '0009_hotels_price_business_hotels_price_econom_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hotels',
            old_name='Price_business',
            new_name='price_business',
        ),
    ]
