# Generated by Django 4.2.4 on 2023-09-16 17:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alter_profile_first_name_alter_profile_last_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='wishlist',
        ),
    ]
