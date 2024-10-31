"""
ASGI config for health_data_project project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os

# Импортирует функцию get_asgi_application из django.core.asgi
from django.core.asgi import get_asgi_application

# Устанавливает настройки окружения по умолчанию для Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'health_data_project.settings')

# Создает объект application, который будет использоваться для обработки ASGI-запросов
application = get_asgi_application()
