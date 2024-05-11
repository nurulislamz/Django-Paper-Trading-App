# Generated by Django 5.0.2 on 2024-05-10 23:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock_data_app', '0005_alter_stockprice_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='stockprice',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 11, 0, 50, 39, 963566)),
        ),
        migrations.AlterField(
            model_name='stockprice',
            name='ticker',
            field=models.CharField(max_length=5, unique=True),
        ),
    ]
