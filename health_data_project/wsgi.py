"""
WSGI config for health_data_project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os

# Импортирует функцию get_wsgi_application из django.core.wsgi
from django.core.wsgi import get_wsgi_application

# Устанавливает настройки окружения по умолчанию для Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'health_data_project.settings')

# Создает объект application, который будет использоваться для обработки WSGI-запросов
application = get_wsgi_application()