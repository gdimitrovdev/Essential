# Django imports
from django.shortcuts import render, redirect
from .models import Todo, File
from .forms import TodoForm, EditForm, FileForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required


@login_required
def home(request):
    # get user's todos
    todo_list = request.user.todos.order_by('date')
    form = TodoForm()

    # get needed forms
    edit_form = EditForm()
    file_form = FileForm()

    # get user's files
    files = request.user.files.order_by('id')

    context = {'todo_list': todo_list, 'form': form, 'editForm': edit_form, 'fileForm': file_form, 'files': files}
    return render(request, "todoapp/home.html", context)


# function to add todos
def add(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            date = request.POST['date_year']+'-'+request.POST['date_month']+'-'+request.POST['date_day']
            new_todo = Todo(user=request.user, text=request.POST['text'], date=date)
            new_todo.save()
    return redirect('../#todo')


# function to delete todos
def delete(request, todo_id):
    item = request.user.todos.get(pk=todo_id)
    item.delete()
    return redirect('../../#todo')


# register new users
def register(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('../')
    context = {"form": form}
    return render(request, "registration/register.html", context)


# edit existing todos
def edit(request, id):
    if request.method == 'POST':
        form = EditForm(request.POST)
        if form.is_valid:
            new_text = request.POST['text']
            new_date = request.POST['date_year']+'-'+request.POST['date_month']+'-'+request.POST['date_day']
            todo = Todo.objects.get(pk=id)
            todo.text = new_text
            todo.date = new_date
            todo.save()
    return redirect('../../#todo')


# add files to user's storage
def filepost(request):
    if request.method == 'POST':
        file_form = FileForm(request.POST, request.FILES)
        if file_form.is_valid():
            newupload = File(user=request.user, file=request.FILES['file'])
            newupload.save()
    return redirect('../#files')


# delete files from storage
def delete_file(request,id):
    file = File.objects.get(pk=id)
    file.delete()
    return redirect('../../#files')
