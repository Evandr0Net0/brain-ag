from enum import unique
from django.db import models

# Create your models here.


class Producer(models.Model):
    id = models.IntegerField(primary_key=True)
    cpforcnpj = models.CharField(max_length=18, blank=False, null=False, unique=True)
    name = models.CharField(max_length=100, blank=False, null=False)
    farm_name = models.CharField(max_length=100, blank=False, null=False)
    city = models.CharField(max_length=100, blank=False, null=False)
    state = models.CharField(max_length=100, blank=False, null=False)
    total_area_hectares = models.FloatField(blank=False, null=False)
    arable_area_hectares = models.IntegerField(blank=False, null=False)
    vegetation_area_hectares = models.IntegerField(blank=False, null=False)
    planted_types = models.CharField(max_length=200)
