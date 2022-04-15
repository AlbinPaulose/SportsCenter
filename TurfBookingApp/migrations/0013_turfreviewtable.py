# Generated by Django 4.0.2 on 2022-04-14 08:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('TurfBookingApp', '0012_delete_turfreview'),
    ]

    operations = [
        migrations.CreateModel(
            name='TurfReviewTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.CharField(max_length=20)),
                ('feedback', models.TextField(blank=True)),
                ('image', models.ImageField(upload_to='review_images')),
                ('reviewed_at', models.DateField(auto_now_add=True)),
                ('turf_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TurfBookingApp.turfdetails')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
