from django import forms
class TodoForm(forms.Form):
    text=forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class':'formclass'}))
    date=forms.DateField()

class EditForm(forms.Form):
    text=forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class':'formclass'}), label='')

class FileForm(forms.Form):
    file=forms.FileField(label='')