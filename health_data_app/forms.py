from django import forms
from .models import HealthData

# Определение формы для модели HealthData, наследующейся от forms.ModelForm
class HealthDataForm(forms.ModelForm):
    class Meta:
        # Указывает модель, для которой создается форма
        model = HealthData
        # Указывает поля модели, которые будут включены в форму
        fields = ['name', 'age', 'weight', 'height', 'blood_pressure', 'cholesterol']