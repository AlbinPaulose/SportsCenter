# Generated by Django 4.0.2 on 2022-03-07 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Index', '0004_alter_productsdetails_product_details'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productsdetails',
            name='product_actual_price',
            field=models.IntegerField(blank=True),
        ),
    ]
