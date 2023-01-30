from django.db import models
from smart_selects.db_fields import GroupedForeignKey
from colorfield.fields import ColorField

class Category(models.Model):
    name_uz = models.CharField(max_length=200, null=True, blank=True)
    name_ru = models.CharField(max_length=200, null=True, blank=True)
    name_en = models.CharField(max_length=200, null=True, blank=True)
    name_ma = models.CharField(max_length=200, null=True, blank=True)
    name_sw = models.CharField(max_length=200, null=True, blank=True)
    description_uz = models.TextField(max_length=2000, null=True, blank=True)
    description_ru = models.TextField(max_length=2000, null=True, blank=True)
    description_en = models.TextField(max_length=2000, null=True, blank=True)
    description_ma = models.TextField(max_length=2000, null=True, blank=True)
    description_sw = models.TextField(max_length=2000, null=True, blank=True)
    image = models.ImageField(null=True)

    def __str__(self):
        return self.name_uz


class SubCategory(models.Model):
    name_uz = models.CharField(max_length=200, null=True, blank=True)
    name_ru = models.CharField(max_length=200, null=True, blank=True)
    name_en = models.CharField(max_length=200, null=True, blank=True)
    name_ma = models.CharField(max_length=200, null=True, blank=True)
    name_sw = models.CharField(max_length=200, null=True, blank=True)
    description_uz = models.TextField(max_length=2000, null=True, blank=True)
    description_ru = models.TextField(max_length=2000, null=True, blank=True)
    description_en = models.TextField(max_length=2000, null=True, blank=True)
    description_ma = models.TextField(max_length=2000, null=True, blank=True)
    description_sw = models.TextField(max_length=2000, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(null=True)

    def __str__(self):
        return f"{self.name_uz}"


class Product(models.Model):
    name_uz = models.CharField(max_length=200, null=True, blank=True)
    name_ru = models.CharField(max_length=200, null=True, blank=True)
    name_en = models.CharField(max_length=200, null=True, blank=True)
    name_ma = models.CharField(max_length=200, null=True, blank=True)
    name_sw = models.CharField(max_length=200, null=True, blank=True)
    description_uz = models.TextField(max_length=2000, null=True, blank=True)
    description_ru = models.TextField(max_length=2000, null=True, blank=True)
    description_en = models.TextField(max_length=2000, null=True, blank=True)
    description_ma = models.TextField(max_length=2000, null=True, blank=True)
    description_sw = models.TextField(max_length=2000, null=True, blank=True)
    color1 = models.CharField(max_length=200, null=True, blank=True)
    color2 = models.CharField(max_length=200, null=True, blank=True)
    color3 = models.CharField(max_length=200, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    sub_category = GroupedForeignKey(SubCategory, 'category', null=True)
    image = models.ImageField(null=True, blank=True)
    image1 = models.ImageField(null=True, blank=True)
    image2 = models.ImageField(null=True, blank=True)
    video = models.FileField(null=True, blank=True)
    product_code = models.CharField(max_length=200, null=True, blank=True)
    price = models.FloatField(default=0)
    persent = models.IntegerField(default=0)
    count = models.IntegerField(default=0)
    minimum = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    top  = models.BooleanField(default=False)

    def __str__(self):
        return self.name_uz


class Slider(models.Model):
    name_uz = models.CharField(max_length=200, null=True, blank=True)
    name_ru = models.CharField(max_length=200, null=True, blank=True)
    name_en = models.CharField(max_length=200, null=True, blank=True)
    name_ma = models.CharField(max_length=200, null=True, blank=True)
    name_sw = models.CharField(max_length=200, null=True, blank=True)
    description_uz = models.TextField(max_length=2000, null=True, blank=True)
    description_ru = models.TextField(max_length=2000, null=True, blank=True)
    description_en = models.TextField(max_length=2000, null=True, blank=True)
    description_ma = models.TextField(max_length=2000, null=True, blank=True)
    description_sw = models.TextField(max_length=2000, null=True, blank=True)
    color = models.CharField(max_length=20, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    url = models.URLField(null=True)


    def __str__(self):
        return self.name_uz


class Nationality(models.Model):
    name_uz = models.CharField(max_length=200, null=True, blank=True)
    name_ru = models.CharField(max_length=200, null=True, blank=True)
    name_en = models.CharField(max_length=200, null=True, blank=True)
    name_ma = models.CharField(max_length=200, null=True, blank=True)
    name_sw = models.CharField(max_length=200, null=True, blank=True)
    description_uz = models.TextField(max_length=2000, null=True, blank=True)
    description_ru = models.TextField(max_length=2000, null=True, blank=True)
    description_en = models.TextField(max_length=2000, null=True, blank=True)
    description_ma = models.TextField(max_length=2000, null=True, blank=True)
    description_sw = models.TextField(max_length=2000, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    url = models.URLField(null=True)


class News(models.Model):
    name_uz = models.CharField(max_length=200, null=True, blank=True)
    name_ru = models.CharField(max_length=200, null=True, blank=True)
    name_en = models.CharField(max_length=200, null=True, blank=True)
    name_ma = models.CharField(max_length=200, null=True, blank=True)
    name_sw = models.CharField(max_length=200, null=True, blank=True)
    description_uz = models.TextField(max_length=2000, null=True, blank=True)
    description_ru = models.TextField(max_length=2000, null=True, blank=True)
    description_en = models.TextField(max_length=2000, null=True, blank=True)
    description_ma = models.TextField(max_length=2000, null=True, blank=True)
    description_sw = models.TextField(max_length=2000, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)


class Event(models.Model):
    name_uz = models.CharField(max_length=200, null=True, blank=True)
    name_ru = models.CharField(max_length=200, null=True, blank=True)
    name_en = models.CharField(max_length=200, null=True, blank=True)
    name_ma = models.CharField(max_length=200, null=True, blank=True)
    name_sw = models.CharField(max_length=200, null=True, blank=True)
    description_uz = models.TextField(max_length=2000, null=True, blank=True)
    description_ru = models.TextField(max_length=2000, null=True, blank=True)
    description_en = models.TextField(max_length=2000, null=True, blank=True)
    description_ma = models.TextField(max_length=2000, null=True, blank=True)
    description_sw = models.TextField(max_length=2000, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)


class Partner(models.Model):
    image = models.ImageField(null=True, blank=True)
    