
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import TodoItem

def todo_view(request):
    all_todo_items = TodoItem.objects.all()
    return render(request, 'todo.html',
        {'all_items': all_todo_items})

def add_todo(request):
    new_item = TodoItem(content = request.POST['content'])
    new_item.save()
    return redirect('/')

def delete_todo(request, pk):
    item_to_delete = TodoItem.objects.get(id=pk)
    item_to_delete.delete()
    return redirect('/')

