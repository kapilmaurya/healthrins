# Generated by Django 4.1.1 on 2022-10-17 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0009_address_first_name_address_last_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='order_items',
            name='price',
            field=models.IntegerField(default=3500),
        ),
        migrations.DeleteModel(
            name='Order_details',
        ),
    ]
