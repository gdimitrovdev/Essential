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
    todo_list=request.user.todos.order_by('date')
    form=TodoForm()

    # get needed forms
    editForm=EditForm()
    fileForm=FileForm()

    # get user's files
    files=request.user.files.order_by('id')

    context={'todo_list':todo_list,'form':form, 'editForm':editForm, 'fileForm':fileForm, 'files':files}
    return render(request,"todoapp/home.html",context)

# function to add todos
def add(request):
    if request.method=='POST':
        form=TodoForm(request.POST)
        if form.is_valid():
            newTodo=Todo(user=request.user,text=request.POST['text'], date=request.POST['date'])
            newTodo.save()
    return redirect('../#todo')

# function to delete todos
def delete(request, todo_id):
    item=request.user.todos.get(pk=todo_id)
    item.delete()
    return redirect('../../#todo')

# register new users
def register(request):
    form=UserCreationForm()
    if request.method=="POST":
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data["username"]
            password=form.cleaned_data["password1"]
            user=authenticate(username=username, password=password)
            login(request,user)
            return redirect('../')
    context={"form":form}
    return render(request,"registration/register.html",context)

# edit existing todos
def edit(request, id):
    form=EditForm()
    if request.method=='POST':
        form=EditForm(request.POST)
        if form.is_valid:
            print(1)
            new_text=request.POST['text']
            todo=Todo.objects.get(pk=id)
            todo.text=new_text
            todo.save()
    return redirect('../../#todo')

# add files to user's storage
def filepost(request):
    fileForm=FileForm()
    if request.method=='POST':
        fileForm=FileForm(request.POST, request.FILES)
        if fileForm.is_valid():
            newupload=File(user=request.user, file=request.FILES['file'])
            newupload.save()
    return redirect('../#files')

# delete files from storage
def deleteFile(request,id):
    file=File.objects.get(pk=id)
    file.delete()
    return redirect('../../#files')