import os
import json
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import HealthDataForm
from .models import HealthData
from django.conf import settings

# Основное представление для главной страницы
def index(request):
    if request.method == 'POST':
        # Создаем форму с данными из POST-запроса
        form = HealthDataForm(request.POST)
        if form.is_valid():
            # Сохраняем данные формы в базе данных
            health_data = form.save()
            # Сохраняем данные в JSON-файл
            save_to_json(health_data)
            # Перенаправляем пользователя на главную страницу
            return redirect('index')
    else:
        # Создаем пустую форму для GET-запроса
        form = HealthDataForm()

    # Получаем список JSON-файлов
    files = get_json_files()
    # Отправляем данные в шаблон
    return render(request, 'health_data_app/index.html', {'form': form, 'files': files})

# Представление для загрузки JSON-файла
def upload_file(request):
    if request.method == 'POST' and request.FILES['file']:
        file = request.FILES['file']
        if file.name.endswith('.json'):
            # Сохраняем файл на сервере
            file_path = os.path.join(settings.STATIC_ROOT, file.name)
            with open(file_path, 'wb+') as destination:
                for chunk in file.chunks():
                    destination.write(chunk)
            # Валидируем JSON-файл
            if validate_json_file(file_path):
                return redirect('index')
            else:
                # Удаляем невалидный файл
                os.remove(file_path)
                return HttpResponse("Invalid JSON file")
        else:
            return HttpResponse("Invalid file format")
    # Отправляем данные в шаблон для загрузки файла
    return render(request, 'health_data_app/upload-file.html')

# Функция для сохранения данных модели в JSON-файл
def save_to_json(health_data):
    file_path = os.path.join(settings.STATIC_ROOT, f'{health_data.name}.json')
    with open(file_path, 'w') as file:
        json.dump(health_data.to_dict(), file)

# Функция для получения списка JSON-файлов
def get_json_files():
    files = []
    for file in os.listdir(settings.STATIC_ROOT):
        if file.endswith('.json'):
            files.append(file)
    return files

# Функция для валидации JSON-файла
def validate_json_file(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            if all(key in data for key in ['name', 'age', 'weight', 'height', 'blood_pressure', 'cholesterol']):
                return True
    except (json.JSONDecodeError, KeyError):
        return False
    return False
