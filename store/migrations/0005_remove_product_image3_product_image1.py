# Generated by Django 4.0.5 on 2022-07-14 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_product_image2_product_image3_product_video'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='image3',
        ),
        migrations.AddField(
            model_name='product',
            name='image1',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]