from django.db import models
from django.core.validators import MinLengthValidator,MaxLengthValidator

# Create your models here.

class Item(models.Model):
    reference = models.PositiveIntegerField(validators=[MaxLengthValidator(12),MinLengthValidator(12)])
    date_exp = models.DateField()
    brand = models.ForeignKey('Brand',null=False, on_delete=models.CASCADE)

class Brand(models.Model):
    name = models.CharField(max_length=255)