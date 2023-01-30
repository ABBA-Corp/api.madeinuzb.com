# Generated by Django 4.0.5 on 2022-07-16 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_nationality_reklama'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_uz', models.CharField(blank=True, max_length=200, null=True)),
                ('name_ru', models.CharField(blank=True, max_length=200, null=True)),
                ('name_en', models.CharField(blank=True, max_length=200, null=True)),
                ('description_uz', models.TextField(blank=True, max_length=2000, null=True)),
                ('description_ru', models.TextField(blank=True, max_length=2000, null=True)),
                ('description_en', models.TextField(blank=True, max_length=2000, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('url', models.URLField(null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Reklama',
        ),
    ]