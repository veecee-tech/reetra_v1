# Generated by Django 3.2.15 on 2022-08-23 12:28

import authentication.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import productReceipt.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Receipt_No',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('receipt_no', models.CharField(blank=True, max_length=500, null=True, unique=True)),
                ('receive_from', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=11)),
                ('is_submitted', models.BooleanField(default=False)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('time_filter', models.TimeField(auto_now_add=True)),
                ('user', models.ForeignKey(default=authentication.models.UserAccount, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='productuser', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=50)),
                ('item_price', models.IntegerField()),
                ('item_qty', models.IntegerField()),
                ('item_desc', models.CharField(max_length=250)),
                ('receipt_no', models.ForeignKey(blank=True, default=productReceipt.models.Receipt_No, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='productreceiptno', to='productReceipt.receipt_no')),
            ],
        ),
    ]
