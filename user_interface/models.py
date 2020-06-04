from django.db import models

class Type(models.Model):
    measurement = models.CharField(max_length=50)

    def __str__(self):
        return self.measurement

class Unit(models.Model):
    type = models.ForeignKey('Type', on_delete=models.CASCADE)
    to_base_unit = models.FloatField()
    unit = models.CharField(max_length=50)

    def __str__(self):
        return self.unit

class BaseUnit(models.Model):
    base_unit = models.ForeignKey('Unit', on_delete=models.CASCADE)
    type = models.ForeignKey('Type', on_delete=models.CASCADE)

    def __str__(self):
        return self.base_unit.unit
