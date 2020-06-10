from django.db import models
from django.contrib.auth.models import User

class Type(models.Model):
    measurement = models.CharField(max_length=50)

    def __str__(self):
        return self.measurement

class Unit(models.Model):
    type = models.ForeignKey('Type', on_delete=models.CASCADE)
    to_base_multiplier = models.FloatField()
    to_base_adder = models.FloatField()
    unit = models.CharField(max_length=50)
    abbreviation = models.CharField(max_length=10)
    description = models.TextField()
    
    def __str__(self):
        return self.unit

class BaseUnit(models.Model):
    base_unit = models.ForeignKey('Unit', on_delete=models.CASCADE)
    type = models.ForeignKey('Type', on_delete=models.CASCADE)

    def __str__(self):
        return self.base_unit.unit

class UpdateCurrency(models.Model):
    timestamp = models.BigIntegerField()

class History(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    source_unit = models.ForeignKey('Unit', on_delete=models.CASCADE, related_name="source")
    source_value = models.CharField(max_length=200)
    destination_unit =  models.ForeignKey('Unit', on_delete=models.CASCADE, related_name="destination")
    destination_value = models.CharField(max_length=200)
    type = models.ForeignKey('Type', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
