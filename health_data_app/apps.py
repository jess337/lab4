from django.apps import AppConfig

# Определение конфигурации приложения HealthDataAppConfig, наследующейся от AppConfig
class HealthDataAppConfig(AppConfig):
    # Устанавливает тип автоинкрементного поля по умолчанию для моделей в этом приложении
    default_auto_field = 'django.db.models.BigAutoField'
    # Устанавливает имя приложения
    name = 'health_data_app'