# Generated by Django 4.1.1 on 2022-09-26 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_alter_product_pack_alter_product_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='pack',
            field=models.CharField(max_length=20),
        ),
    ]
