# Generated by Django 4.0.2 on 2022-04-01 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TurfBookingApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TurfDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('Football', 'football'), ('Shuttle', 'shuttle'), ('Cricket', 'cricket')], max_length=20)),
                ('turf_name', models.CharField(max_length=50)),
                ('turf_place', models.CharField(max_length=50)),
                ('turf_morningPrice', models.IntegerField()),
                ('turf_eveningPrice', models.IntegerField()),
                ('turf_phoneNumber', models.CharField(max_length=10)),
                ('turf_address', models.CharField(max_length=70)),
            ],
        ),
        migrations.DeleteModel(
            name='FootballTurfDetails',
        ),
    ]
