# Generated by Django 4.1.1 on 2022-09-26 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_alter_product_pack'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='pack',
        ),
        migrations.AddField(
            model_name='product',
            name='pack2',
            field=models.IntegerField(default=20),
        ),
        migrations.AddField(
            model_name='product',
            name='pack3',
            field=models.IntegerField(default=30),
        ),
    ]
