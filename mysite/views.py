from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from .models import ToDo


def index(request):
    todos = ToDo.objects.all()
    return render(request, 'mysite/index.html', {'todo_list': todos, 'title': 'Главная страница'})


@require_http_methods(['POST'])
@csrf_exempt
def add(request):
    title = request.POST['title']
    description = request.POST.get('description')
    deadline = request.POST['deadline']
    if deadline == "":
        deadline = None
    todo = ToDo(title=title, description=description, deadline=deadline)
    todo.save()
    return redirect('index')


def edit(request, todo_id):
    todos = ToDo.objects.get(id=todo_id)
    context = {'todos': todos, 'title': 'Редактирование'}
    return render(request, 'mysite/edit.html', context)


def delete(request, todo_id):
    todo = ToDo.objects.get(id=todo_id)
    todo.delete()
    return redirect('index')


def finished(request, todo_id):
    todo = ToDo.objects.get(id=todo_id)
    todo.is_complete = not todo.is_complete
    todo.save()
    return redirect('index')


def update(request, todo_id):
    todo = ToDo.objects.get(id=todo_id)
    todo.title = request.POST['title']
    todo.description = request.POST['description']
    todo.deadline = request.POST['deadline']
    todo.is_complete = request.POST.get('is_complete')
    if todo.deadline == "":
        todo.deadline = None
    if todo.is_complete is None:
        todo.is_complete = False
    elif todo.is_complete is not None:
        todo.is_complete = True
    todo.save()
    print(todo.is_complete)
    return redirect('index')
