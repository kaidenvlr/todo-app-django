from django.shortcuts import get_object_or_404, redirect, render

from profiles.models import ProfileCategory
from tasks.forms import TaskForm
from tasks.models import Task


def create_task_view(request, pk):
    task_list = get_object_or_404(ProfileCategory, pk=pk)
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.task_list = task_list
            task.save()
            return redirect('list', pk=pk)
    else:
        form = TaskForm()
    return render(request, 'tasks/create-task.html', {'form': form})


def delete_task_view(request, pk, task_id):
    task = get_object_or_404(Task, pk=task_id)
    task.delete()
    return redirect('list', pk=pk)


def complete_task_view(request, pk, task_id):
    task = get_object_or_404(Task, pk=task_id)
    task.is_done = True
    task.save()
    return redirect('list', pk=pk)


def incomplete_task_view(request, pk, task_id):
    task = get_object_or_404(Task, pk=task_id)
    task.is_done = False
    task.save()
    return redirect('list', pk=pk)
