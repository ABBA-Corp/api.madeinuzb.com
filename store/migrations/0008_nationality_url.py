# Generated by Django 4.0.5 on 2022-07-19 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_slider_delete_reklama'),
    ]

    operations = [
        migrations.AddField(
            model_name='nationality',
            name='url',
            field=models.URLField(null=True),
        ),
    ]
