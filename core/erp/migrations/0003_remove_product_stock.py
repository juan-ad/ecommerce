# Generated by Django 4.1.7 on 2023-03-06 23:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0002_category_client_detsale_product_sale_delete_employee_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='stock',
        ),
    ]
