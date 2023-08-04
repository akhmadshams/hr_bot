from django import forms
from .models import Staff, ToDo

class StaffForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = '__all__'

class TodoForm(forms.ModelForm):
    class Meta:
        model = ToDo
        fields = ['task']
