from django.db import models
from django.contrib.auth.models import User

class Type(models.Model):
    # define a type of measurement, e.g. length or mass conversion
    measurement = models.CharField(max_length=50)

    # in the admin panel, display the measurement type instead of the object ID
    def __str__(self):
        return self.measurement

class Unit(models.Model):
    # define a unit, e.g. meter, kilogram
    type = models.ForeignKey('Type', on_delete=models.CASCADE)
    to_base_multiplier = models.FloatField()
    to_base_adder = models.FloatField()
    unit = models.CharField(max_length=50)
    abbreviation = models.CharField(max_length=10)
    description = models.TextField()

    # in the admin panel, display the unit instead of the object ID
    def __str__(self):
        return self.unit

class BaseUnit(models.Model):
    # define a base unit used for conversions, e.g. kilogram is the base unit of mass
    base_unit = models.ForeignKey('Unit', on_delete=models.CASCADE)
    type = models.ForeignKey('Type', on_delete=models.CASCADE)

    # in the admin panel, display the base unit instead of the object ID
    def __str__(self):
        return self.base_unit.unit

class UpdateCurrency(models.Model):
    # stores the timestamp of the last time the currency exchange rates have been updated
    timestamp = models.BigIntegerField()

class History(models.Model):
    # define a query in the user history, specific to the logged in user
    timestamp = models.DateTimeField(auto_now_add=True)
    source_unit = models.ForeignKey('Unit', on_delete=models.CASCADE, related_name="source")
    source_value = models.CharField(max_length=200)
    destination_unit =  models.ForeignKey('Unit', on_delete=models.CASCADE, related_name="destination")
    destination_value = models.CharField(max_length=200)
    type = models.ForeignKey('Type', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
