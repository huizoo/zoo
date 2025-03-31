from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoForm


def index(request):
    works=Todo.objects.all()
    context = {
        'todo_list': works
    }
    return render(request, 'todos/index.html', context)

def create_todo(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save()
            return redirect('todos:detail', todo.pk)
    else:
        form = TodoForm()

    context = {
        'form': form,
    }
    return render(request, 'todos/create_todo.html', context)

def detail(request, todo_pk):
    todo=Todo.objects.get(pk=todo_pk)
    context = {
        'todo': todo
    }
    return render(request, 'todos/detail.html', context)

def delete_todo(request, todo_pk):
    todo = Todo.objects.get(pk=todo_pk)
    if request.method == 'POST':
        todo.delete()
        return redirect('todos:index')
    else:
        return redirect('todos:detail', todo.pk)

def update_todo(request, todo_pk):
    todo = Todo.objects.get(pk=todo_pk)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            todo = form.save()
            return redirect('todos:detail', todo.pk)
    else:
        form = TodoForm(instance=todo)
    context = {
        'todo': todo,
        'form': form,
    }
    return render(request, 'todos/update_todo.html', context)