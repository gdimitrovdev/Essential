# Django imports
from django.shortcuts import render, redirect
from .models import Todo, File, DailyTask
from .forms import TodoForm, EditForm, FileForm, DailyTaskForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.http import JsonResponse, FileResponse


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

    # get user's daily tasks
    daily_tasks = request.user.daily_tasks.all()
    daily_task_form = DailyTaskForm()

    context = {
        'todo_list': todo_list,
        'form': form,
        'editForm': edit_form,
        'fileForm': file_form,
        'files': files,
        'dailyTasks': daily_tasks,
        'dailyTasksForm': daily_task_form
               }
    return render(request, "todoapp/home.html", context)


@login_required
# function to add todos
def add_todo(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            date = request.POST['date_year']+'-'+request.POST['date_month']+'-'+request.POST['date_day']
            new_todo = Todo(user=request.user, text=request.POST['text'], date=date)
            new_todo.save()
    return redirect('../#todo')


@login_required
# function to delete todos
def delete_todo(request):
    id = request.GET.get('id', None)
    item = request.user.todos.get(pk=id)
    item.delete()
    data = {}
    return JsonResponse(data)


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


@login_required
# edit existing todos
def edit_todo(request, id):
    if request.method == 'POST':
        form = EditForm(request.POST)
        if form.is_valid:
            new_text = request.POST['text']
            new_date = request.POST['date_year']+'-'+request.POST['date_month']+'-'+request.POST['date_day']
            todo = Todo.objects.get(pk=id)

            # check if the action is illegal
            if todo.user != request.user:
                return redirect('/')

            todo.text = new_text
            todo.date = new_date
            todo.save()
    return redirect('../../#todo')


@login_required
# add files to user's storage
def filepost(request):
    if request.method == 'POST':
        file_form = FileForm(request.POST, request.FILES)
        if file_form.is_valid():
            newupload = File(user=request.user, file=request.FILES['file'])
            newupload.save()
    return redirect('../#files')


@login_required
# delete files from storage
def delete_file(request,id):
    file = File.objects.get(pk=id)

    # check if this is an invalid action
    if file.user != request.user:
        return redirect('/')

    file.delete()
    return redirect('../../#files')


@login_required
# create daily task
def add_daily_task(request):
    if request.method == 'POST':
        form = DailyTaskForm(request.POST)
        if form.is_valid():
            new_daily_task = form.save()
            new_daily_task.user = request.user
            new_daily_task.save()
    return redirect('../#daily')


@login_required
# mark daily task as completed
def completed(request):
    id = request.GET.get('id', None)
    task = DailyTask.objects.get(pk=id)
    if task.completed_today:
        task.last_completed = None
    else:
        task.last_completed = timezone.datetime.now().date()
    task.save()
    data = {}
    return JsonResponse(data)


@login_required
# delete daily task
def delete_task(request):
    id = request.GET.get('id', None)
    task = DailyTask.objects.get(pk=id)
    task.delete()
    data = {}
    return JsonResponse(data)


@login_required
# download view
def download(request, file_id):
    file = File.objects.get(pk=file_id)
    print(file.file.path)
    return FileResponse(open(file.file.path, 'rb'))
