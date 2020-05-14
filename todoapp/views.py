from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
	todo_list=request.user.todos.order_by('id')
	form=TodoForm()
	context={'todo_list':todo_list,'form':form}
	return render(request,"todoapp/home.html",context)
	
def add(request):
	if request.method=='POST':
		form=TodoForm(request.POST)
		if form.is_valid:
			newTodo=Todo(user=request.user,text=request.POST['text'])
			newTodo.save()
			return redirect('../#todo')

def delete(request, todo_id):
	item=request.user.todos.get(pk=todo_id)
	item.delete()
	return redirect('../../#todo')
	
def register(request):
	form=UserCreationForm()
	if request.method=="POST":
		form=UserCreationForm(request.POST)
		if form.is_valid:
			form.save()
			username=form.cleaned_data["username"]
			password=form.cleaned_data["password1"]
			user=authenticate(username=username, password=password)
			login(request,user)
	context={"form":form}
	return render(request,"registration/register.html",context)