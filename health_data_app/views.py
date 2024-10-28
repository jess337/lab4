import os
import json
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import HealthDataForm
from .models import HealthData
from django.conf import settings

def index(request):
    if request.method == 'POST':
        form = HealthDataForm(request.POST)
        if form.is_valid():
            health_data = form.save()
            save_to_json(health_data)
            return redirect('index')
    else:
        form = HealthDataForm()

    files = get_json_files()
    return render(request, 'health_data_app/index.html', {'form': form, 'files': files})

def upload_file(request):
    if request.method == 'POST' and request.FILES['file']:
        file = request.FILES['file']
        if file.name.endswith('.json'):
            file_path = os.path.join(settings.STATIC_ROOT, file.name)
            with open(file_path, 'wb+') as destination:
                for chunk in file.chunks():
                    destination.write(chunk)
            if validate_json_file(file_path):
                return redirect('index')
            else:
                os.remove(file_path)
                return HttpResponse("Invalid JSON file")
        else:
            return HttpResponse("Invalid file format")
    return render(request, 'health_data_app/upload-file.html')

def save_to_json(health_data):
    file_path = os.path.join(settings.STATIC_ROOT, f'{health_data.name}.json')
    with open(file_path, 'w') as file:
        json.dump(health_data.to_dict(), file)

def get_json_files():
    files = []
    for file in os.listdir(settings.STATIC_ROOT):
        if file.endswith('.json'):
            files.append(file)
    return files

def validate_json_file(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            if all(key in data for key in ['name', 'age', 'weight', 'height', 'blood_pressure', 'cholesterol']):
                return True
    except (json.JSONDecodeError, KeyError):
        return False
    return False
