# Generated by Django 4.1.7 on 2023-03-07 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0003_remove_product_stock'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='dni',
            field=models.CharField(max_length=10, unique=True, verbose_name='Cedula'),
        ),
    ]
