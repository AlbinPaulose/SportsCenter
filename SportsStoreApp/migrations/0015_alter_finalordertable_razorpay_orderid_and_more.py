# Generated by Django 4.0.2 on 2022-04-25 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SportsStoreApp', '0014_finalordertable_razorpay_paymentid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='finalordertable',
            name='razorpay_orderId',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='finalordertable',
            name='razorpay_paymentId',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='finalordertable',
            name='razorpay_signatureId',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
