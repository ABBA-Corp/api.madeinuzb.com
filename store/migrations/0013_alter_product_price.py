# Generated by Django 4.0.5 on 2022-07-25 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0012_rename_mimnimum_product_minimum'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.FloatField(default=0),
        ),
    ]
