#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""

# Импортирует необходимые модули
import os
import sys

# Основная функция, которая выполняет административные задачи
def main():
    """Run administrative tasks."""

    # Устанавливает настройки окружения по умолчанию для Django
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'health_data_project.settings')

    try:
        # Попытка импортировать модуль execute_from_command_line из Django
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        # Обработка исключения, если импорт не удался
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

    # Выполнение командной строки Django
    execute_from_command_line(sys.argv)

# Проверка, запускается ли скрипт напрямую
if __name__ == '__main__':
    main()
