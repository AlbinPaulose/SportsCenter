# Generated by Django 4.0.2 on 2022-03-07 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Index', '0003_productsdetails_product_details'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productsdetails',
            name='product_details',
            field=models.TextField(blank=True, max_length=200),
        ),
    ]