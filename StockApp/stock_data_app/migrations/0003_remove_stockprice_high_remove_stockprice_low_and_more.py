# Generated by Django 5.0.2 on 2024-05-10 23:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock_data_app', '0002_rename_market_stock_description_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stockprice',
            name='high',
        ),
        migrations.RemoveField(
            model_name='stockprice',
            name='low',
        ),
        migrations.RemoveField(
            model_name='stockprice',
            name='volume',
        ),
        migrations.AlterField(
            model_name='stockprice',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 11, 0, 8, 44, 649200)),
        ),
    ]
