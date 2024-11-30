from django.shortcuts import render, redirect, get_object_or_404
from . models import Todo
from .forms import TodoForm

def todo_list(request):
    todo_list = Todo.objects.all()
    if request.method =='POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home:todo_list')
    else: 
            form = TodoForm()
        
    return render(request,'todo_list.html', {
        'todo_list':todo_list,
        'form': form,
        })
        

