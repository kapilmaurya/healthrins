# Generated by Django 4.1.1 on 2022-09-17 21:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_profile_remove_user_payments_user_id_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='lastname',
            new_name='username',
        ),
    ]
