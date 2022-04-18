from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.


class Item(models.Model):
    reference = models.PositiveIntegerField(validators=[MaxValueValidator(99999999), MinValueValidator(10000000)])
    date_exp = models.DateField()
    brand = models.CharField(max_length=255)



