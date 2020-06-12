from django import forms
from .models import student
class taskform(forms.ModelForm):
    class Meta:
        model = student
        fields = ['name', 'work_to_do', 'deadline']
