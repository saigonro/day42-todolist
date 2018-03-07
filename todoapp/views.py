from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import TodoItem
from .forms import TodoItemForm

# Create your views here.

def get_todo(request):
    if request.method == "POST":
        form = TodoItemForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = TodoItemForm()
    
    items = TodoItem.objects.all()
    return render(request, "todoapp/todo.html", {'items': items, 'form': form})
    
def delete_todo_item(request, id):
    item = get_object_or_404(TodoItem, pk=id)
    item.delete()
    return HttpResponse("You deleted " + item.name)
