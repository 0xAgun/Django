# Generated by Django 4.0.1 on 2022-01-09 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_product_mg'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='mg',
            field=models.CharField(max_length=100),
        ),
    ]