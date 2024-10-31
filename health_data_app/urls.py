# Импортируем модуль path из django.urls для создания URL-ов
from django.urls import path

# Импортируем модуль views из текущего приложения для использования представлений
from . import views

# Список URL-ов и соответствующих представлений
urlpatterns = [
    # URL для главной страницы
    path('', views.index, name='index'),

    # URL для страницы загрузки JSON-файла
    path('upload/', views.upload_file, name='upload'),
]
