# Generated by Django 4.1 on 2022-09-01 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_hotel', '0010_rename_price_business_hotels_price_business'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_user', models.CharField(max_length=30, verbose_name='Имя')),
                ('email_user', models.EmailField(max_length=30, verbose_name='Email')),
                ('time_go', models.DateField(verbose_name='Дата Вылета')),
                ('time_back', models.DateField(verbose_name='Дата Прилета')),
            ],
        ),
    ]
