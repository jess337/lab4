from django import forms
from .models import HealthData

class HealthDataForm(forms.ModelForm):
    class Meta:
        model = HealthData
        fields = ['name', 'age', 'weight', 'height', 'blood_pressure', 'cholesterol']
