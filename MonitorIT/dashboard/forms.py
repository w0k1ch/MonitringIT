from django import  forms
from .models import Tasks, Execution
from unicodedata import category

from . models import Tasks

class TasksForm(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = ['name', 'category', 'quantity']

class ExecutionForm(forms.ModelForm):
    class Meta:
        model = Execution
        fields = ['Tasks', 'execution_quantity']