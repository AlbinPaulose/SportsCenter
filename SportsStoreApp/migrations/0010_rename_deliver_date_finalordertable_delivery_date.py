# Generated by Django 4.0.2 on 2022-04-23 05:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SportsStoreApp', '0009_rename_paymentid_finalordertable_payment_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='finalordertable',
            old_name='deliver_date',
            new_name='delivery_date',
        ),
    ]
