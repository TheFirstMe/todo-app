from django.shortcuts import render, redirect

from .models import Todolist

from django.views.decorators.http import require_POST

from .forms import TodoListForm

# Create your views here.


def index(request):
    todo_items = Todolist.objects.order_by('id')
    form = TodoListForm()
    # print(form.)
    context = {'todo_items': todo_items, 'form': form}
    return render(request, 'todolist/index.html', context=context)


@require_POST
def addTodoItem(request):
    form = TodoListForm(request.POST)
    if form.is_valid():
        todo_item = Todolist(text=request.POST['text'])
        todo_item.save()

    return redirect('index')


def completedTodo(request, todo_id):
    todo = Todolist.objects.get(pk=todo_id)
    todo.completed = not todo.completed
    todo.save()

    return redirect('index')


def deleteCompleted(request):
    Todolist.objects.filter(completed__exact=True).delete()

    return redirect('index')

def delete(request):
    Todolist.objects.all().delete()

    return redirect('index')
