# Импортируем модуль admin из Django
from django.contrib import admin

# Импортируем модель HealthData из текущего приложения
from .models import HealthData

# Регистрируем модель HealthData в админке Django
# Это позволяет управлять объектами модели через админский интерфейс
admin.site.register(HealthData)