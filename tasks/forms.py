from django import forms
from .models import *
from django.forms import ModelForm

class TaskForm(forms.ModelForm):
    class Meta:
        model = List
        fields = '__all__'
