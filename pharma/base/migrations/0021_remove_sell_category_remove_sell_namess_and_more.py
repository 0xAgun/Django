# Generated by Django 4.0.1 on 2022-01-13 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0020_alter_product_stock'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sell',
            name='category',
        ),
        migrations.RemoveField(
            model_name='sell',
            name='namess',
        ),
        migrations.AlterField(
            model_name='product',
            name='stock',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='sell',
            name='sell_quantity',
            field=models.PositiveIntegerField(blank=True),
        ),
    ]
