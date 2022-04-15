# Generated by Django 4.0.2 on 2022-03-30 19:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Index', '0006_alter_productsdetails_product_size'),
        ('SportsStoreApp', '0004_alter_carttable_user_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='WishlistTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('created_at', models.DateField(auto_now_add=True)),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Index.productsdetails')),
            ],
        ),
    ]
