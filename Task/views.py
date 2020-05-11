from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required



def index_view(request):
    return render(request, 'index.html')
    

def about_view(request):
    return render(request, 'about.html')



@login_required()
def todolist_view(request):
    form = TaskForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save(commit=False).owner = request.user
            form.save()
            messages.success(request, 'New task added!')
    all_tasks = Task.objects.filter(owner=request.user)
    return render(request, 'todolist.html', {'all_tasks':all_tasks, 'form':form})

@login_required
def edit_view(request, task_id):
    task_obj = Task.objects.get(pk=task_id)
    form = TaskForm(request.POST or None, instance=task_obj)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, 'task edited!')
            return redirect('todo')
    return render(request, 'edit.html', {'form':form, 'task_obj':task_obj})

@login_required
def delete_view(request, task_id):
    task = Task.objects.get(pk=task_id)
    if task.owner == request.user:
        task.delete()
    else:
        messages.warning(request, ('Not allowed. Access denied!'))
    return redirect('todo')
    

@login_required
def pending_view(request, task_id):
    task = Task.objects.get(pk=task_id)
    if task.owner == request.user:
        task.done = False
        task.save()
    else:
      messages.warning(request, ('Not allowed. Access denied!'))  
    return redirect('todo')

@login_required
def done_view(request, task_id):
    task = Task.objects.get(pk=task_id)
    if task.owner == request.user:
        task.done = True
        task.save()
    else:
        messages.warning(request, ('Not allowed. Access denied!'))    
    return redirect('todo')

