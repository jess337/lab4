
from django.db import models

class HealthData(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    weight = models.FloatField()
    height = models.FloatField()
    blood_pressure = models.CharField(max_length=10)
    cholesterol = models.FloatField()

    def to_dict(self):
        return {
            'name': self.name,
            'age': self.age,
            'weight': self.weight,
            'height': self.height,
            'blood_pressure': self.blood_pressure,
            'cholesterol': self.cholesterol,
        }
