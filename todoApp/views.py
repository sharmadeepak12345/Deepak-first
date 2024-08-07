from django.shortcuts import get_object_or_404, redirect, render
from .models import Todo
# Create your views here.
def addTask(request):
    task = request.POST['task']
    Todo.objects.create(task=task)
    return redirect('home')
def markDone(request,pk):
    task = get_object_or_404(Todo,pk=pk)
    task.is_completed = True
    task.save()
    return redirect('home')

def mark_unDone(request,pk):
    task = get_object_or_404(Todo,pk=pk)
    task.is_completed = False
    task.save()
    return redirect('home')

def remove_task(request,pk):
    task = get_object_or_404(Todo,pk=pk)
    task.delete()
    return redirect('home')
    
def edit_task(request,pk):
    get_task = get_object_or_404(Todo,pk=pk)
    if request.method=='POST':
        new_task = request.POST['task']
        get_task.task = new_task
        get_task.save()
        return redirect('home')
    else:
        context ={
            'get_task':get_task,
        }
    return render(request,'edit_task.htm',context)