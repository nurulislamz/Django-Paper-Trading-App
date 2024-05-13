# Generated by Django 5.0.2 on 2024-05-11 02:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock_data_app', '0007_alter_stockprice_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='APICount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(default=0)),
                ('date', models.DateTimeField(default=datetime.datetime(2024, 5, 11, 3, 56, 4, 91052))),
            ],
        ),
        migrations.AlterField(
            model_name='stockprice',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 11, 3, 56, 4, 91052)),
        ),
    ]