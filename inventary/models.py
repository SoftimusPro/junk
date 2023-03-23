from django.db import models

# Create your models here.

class CarsBrands(models.Model):
    brand_name = models.CharField(max_length=100)
    country_of_origin = models.CharField(max_length=100)


class Cars(models.Model):
    brand = models.ForeignKey(CarsBrands, on_delete=models.CASCADE)
    _model = models.CharField(max_length=100)
    year = models.IntegerField


class EntryCars(models.Model):
    brand = models.CharField(max_length=100)
    model_car = models.CharField(max_length=100)
    image = models.ImageField(upload_to="")