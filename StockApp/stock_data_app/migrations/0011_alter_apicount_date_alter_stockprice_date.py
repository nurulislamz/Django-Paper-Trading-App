# Generated by Django 5.0.2 on 2024-05-11 11:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock_data_app', '0010_alter_apicount_date_alter_stockprice_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apicount',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 11, 12, 43, 1, 950067)),
        ),
        migrations.AlterField(
            model_name='stockprice',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 11, 12, 43, 1, 950067)),
        ),
    ]
