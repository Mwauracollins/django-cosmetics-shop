# Generated by Django 4.2 on 2023-09-02 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_rename_product_image_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(height_field=200, null=True, upload_to='products', width_field=268),
        ),
    ]
