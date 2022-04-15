# Generated by Django 4.0.2 on 2022-04-01 07:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('TurfBookingApp', '0002_turfdetails_delete_footballturfdetails'),
    ]

    operations = [
        migrations.AddField(
            model_name='footballtimeslottable',
            name='turf_name',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='TurfBookingApp.turfdetails'),
            preserve_default=False,
        ),
    ]