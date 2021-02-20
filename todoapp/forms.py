# Django imports
from django import forms


# form to make a new to-do
class TodoForm(forms.Form):
    text = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'formclass'}), label="Enter text:")
    date = forms.DateField(widget=forms.SelectDateWidget, label='Enter Date:')


# form to edit to-do
class EditForm(forms.Form):
    text = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'formclass'}), label='')
    date = forms.DateField(label='', widget=forms.SelectDateWidget)


# form to add files to the storage
class FileForm(forms.Form):
    file = forms.FileField(label='')
