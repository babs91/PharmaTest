# Generated by Django 3.2.3 on 2022-01-25 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pharma_app', '0003_customer_orders_customers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customers',
            name='Tel',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='customers',
            name='address',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='customers',
            name='email',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='customers',
            name='first_name',
            field=models.CharField(max_length=200),
        ),
    ]