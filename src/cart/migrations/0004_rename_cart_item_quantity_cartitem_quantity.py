# Generated by Django 4.2.4 on 2023-09-14 15:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0003_cart_session_key'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cartitem',
            old_name='cart_item_quantity',
            new_name='quantity',
        ),
    ]