# Generated by Django 4.1.1 on 2022-09-21 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_rename_lastname_profile_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='pack',
            field=models.DecimalField(decimal_places=0, max_digits=2),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=7),
        ),
    ]
