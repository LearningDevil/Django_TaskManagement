from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Task
from .forms import TaskForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required


def home(request):
    if request.user.is_authenticated:
        return redirect('index')  # Redirect to index if already logged in

    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')  # Redirect to index after login
    else:
        form = AuthenticationForm()

    return render(request, "home.html")

def logout_view(request):
    logout(request)
    return redirect('home')

def index(request):
    form = TaskForm()
    tasks = Task.objects.all()

    if request.method == 'POST':
        form = TaskForm(request.POST)

        if form.is_valid():
            form.save()
        return redirect('index')

    context = {'tasks': tasks, 'TaskForm': form}
    return render(request, 'tasks.html', context)


def updateTask(request, pk):
    
    task = Task.objects.get(id = pk)
    form = TaskForm(instance=task)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('index')
    
    context = {'TaskForm': form}
    return render(request, 'update_task.html', context)


def deleteTask(request, pk):
    
    task = Task.objects.get(id = pk)
    if request.method == 'POST':
        task.delete()
        return redirect('index')
    context = {'task': task}
    return render(request, 'delete_task.html', context)
