from Tools.scripts.make_ctype import method
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import  *

def index(request):
    list = List.objects.all()
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {
        'list': list,
        'form': form
    }
    it = List.objects.filter(title='aldl')
    print(it)
    # for e in list:
    #     print(e)
    return render(request, 'tasks/task_list.html', context)


def update_task(request, task_id):
    task = List.objects.get(id=task_id)

    form = TaskForm(instance=task)

    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {
        # 'task': task,
        'form': form
    }
    return render(request, 'tasks/update_task.html', context)


def delete_tasks(request, task_id):
    item = List.objects.get(id = task_id)

    if request.method == 'POST':
        item.delete()
        return redirect('/')

    context = {
        'item': item
    }

    return render(request, 'tasks/delete_task.html', context)


