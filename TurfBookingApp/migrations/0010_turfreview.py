<<<<<<< HEAD
# Generated by Django 4.0.2 on 2022-04-14 08:06
=======
# Generated by Django 4.0.2 on 2022-04-13 19:03
>>>>>>> bab2c48 (review upgraded)

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('TurfBookingApp', '0009_crickettimeslottable'),
    ]

    operations = [
        migrations.CreateModel(
            name='TurfReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
<<<<<<< HEAD
                ('rating', models.CharField(max_length=20)),
                ('feedback', models.TextField(blank=True)),
                ('image', models.ImageField(upload_to='review_images')),
                ('reviewed_at', models.DateField(auto_now_add=True)),
                ('turf', models.CharField(max_length=50)),
=======
                ('rating', models.CharField(max_length=15)),
                ('feedback', models.TextField(blank=True)),
>>>>>>> bab2c48 (review upgraded)
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
