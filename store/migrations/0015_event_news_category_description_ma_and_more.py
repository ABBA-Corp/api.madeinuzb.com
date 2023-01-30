# Generated by Django 4.0.5 on 2022-08-15 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0014_product_product_code'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_uz', models.CharField(blank=True, max_length=200, null=True)),
                ('name_ru', models.CharField(blank=True, max_length=200, null=True)),
                ('name_en', models.CharField(blank=True, max_length=200, null=True)),
                ('name_ma', models.CharField(blank=True, max_length=200, null=True)),
                ('name_sw', models.CharField(blank=True, max_length=200, null=True)),
                ('description_uz', models.TextField(blank=True, max_length=2000, null=True)),
                ('description_ru', models.TextField(blank=True, max_length=2000, null=True)),
                ('description_en', models.TextField(blank=True, max_length=2000, null=True)),
                ('description_ma', models.TextField(blank=True, max_length=2000, null=True)),
                ('description_sw', models.TextField(blank=True, max_length=2000, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_uz', models.CharField(blank=True, max_length=200, null=True)),
                ('name_ru', models.CharField(blank=True, max_length=200, null=True)),
                ('name_en', models.CharField(blank=True, max_length=200, null=True)),
                ('name_ma', models.CharField(blank=True, max_length=200, null=True)),
                ('name_sw', models.CharField(blank=True, max_length=200, null=True)),
                ('description_uz', models.TextField(blank=True, max_length=2000, null=True)),
                ('description_ru', models.TextField(blank=True, max_length=2000, null=True)),
                ('description_en', models.TextField(blank=True, max_length=2000, null=True)),
                ('description_ma', models.TextField(blank=True, max_length=2000, null=True)),
                ('description_sw', models.TextField(blank=True, max_length=2000, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.AddField(
            model_name='category',
            name='description_ma',
            field=models.TextField(blank=True, max_length=2000, null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='description_sw',
            field=models.TextField(blank=True, max_length=2000, null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='name_ma',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='name_sw',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='nationality',
            name='description_ma',
            field=models.TextField(blank=True, max_length=2000, null=True),
        ),
        migrations.AddField(
            model_name='nationality',
            name='description_sw',
            field=models.TextField(blank=True, max_length=2000, null=True),
        ),
        migrations.AddField(
            model_name='nationality',
            name='name_ma',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='nationality',
            name='name_sw',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='description_ma',
            field=models.TextField(blank=True, max_length=2000, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='description_sw',
            field=models.TextField(blank=True, max_length=2000, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='name_ma',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='name_sw',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='slider',
            name='description_ma',
            field=models.TextField(blank=True, max_length=2000, null=True),
        ),
        migrations.AddField(
            model_name='slider',
            name='description_sw',
            field=models.TextField(blank=True, max_length=2000, null=True),
        ),
        migrations.AddField(
            model_name='slider',
            name='name_ma',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='slider',
            name='name_sw',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='subcategory',
            name='description_ma',
            field=models.TextField(blank=True, max_length=2000, null=True),
        ),
        migrations.AddField(
            model_name='subcategory',
            name='description_sw',
            field=models.TextField(blank=True, max_length=2000, null=True),
        ),
        migrations.AddField(
            model_name='subcategory',
            name='name_ma',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='subcategory',
            name='name_sw',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
