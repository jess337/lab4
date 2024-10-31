from django.db import models

# Определение модели HealthData, наследующейся от models.Model
class HealthData(models.Model):
    # Поле для хранения имени (строка максимальной длины 100 символов)
    name = models.CharField(max_length=100)

    # Поле для хранения возраста (целое число)
    age = models.IntegerField()

    # Поле для хранения веса (вещественное число)
    weight = models.FloatField()

    # Поле для хранения роста (вещественное число)
    height = models.FloatField()

    # Поле для хранения артериального давления (строка максимальной длины 10 символов)
    blood_pressure = models.CharField(max_length=10)

    # Поле для хранения уровня холестерина (вещественное число)
    cholesterol = models.FloatField()

    # Метод для преобразования объекта модели в словарь
    def to_dict(self):
        return {
            'name': self.name,
            'age': self.age,
            'weight': self.weight,
            'height': self.height,
            'blood_pressure': self.blood_pressure,
            'cholesterol': self.cholesterol,
        }
