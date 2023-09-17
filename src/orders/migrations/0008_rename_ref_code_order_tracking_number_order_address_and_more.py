# Generated by Django 4.2.4 on 2023-09-13 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0007_alter_orderitem_product'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='ref_code',
            new_name='tracking_number',
        ),
        migrations.AddField(
            model_name='order',
            name='address',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='first_name',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='last_name',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='order_status',
            field=models.CharField(choices=[('Delivered', 'Delivered'), ('Shipping', 'Shipping'), ('Pending', 'Pending')], max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='payment_method',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='phone_number',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='region',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='town',
            field=models.CharField(max_length=250, null=True),
        ),
    ]