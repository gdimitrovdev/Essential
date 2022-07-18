# Django imports
from django import forms
from .models import DailyTask


# form to make a new to-do
class TodoForm(forms.Form):
    text = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'formclass'}), label="Enter text:")
    date = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}), label='Enter Date:')


# form to edit to-do
class EditForm(forms.Form):
    text = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'formclass'}), label='', required=False)
    date = forms.DateField(label='', widget=forms.widgets.DateInput(attrs={'type': 'date'}), required=False)


# form to add files to the storage
class FileForm(forms.Form):
    file = forms.FileField(label='')


# form to create a daily repeating task
class DailyTaskForm(forms.ModelForm):
    class Meta:
        model = DailyTask
        fields = ['text']
