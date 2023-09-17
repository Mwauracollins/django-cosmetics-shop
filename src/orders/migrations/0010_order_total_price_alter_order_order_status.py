# Generated by Django 4.2 on 2023-09-13 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0009_order_created_at_order_email_order_payment_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='total_price',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_status',
            field=models.CharField(choices=[('Delivered', 'Delivered'), ('Shipping', 'Shipping'), ('Pending', 'Pending')], default='Pending', max_length=150, null=True),
        ),
    ]
