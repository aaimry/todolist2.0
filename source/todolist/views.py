from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseNotFound

from forms import ToDoListForm
from todolist.models import ToDoList


def todolist_view(request):
    aim_list = ToDoList.objects.all()
    return render(request, 'todolist.html', {'aim_list': aim_list})


def create_todolist_view(request):
    if request.method == 'GET':
        form = ToDoListForm()
        return render(request, 'todolist_create.html', {'form': form})
    else:
        form = ToDoListForm(data=request.POST)
        if form.is_valid():
            aim = form.cleaned_data.get('aim')
            status = form.cleaned_data.get('status')
            deadline_at = form.cleaned_data.get('deadline_at')
            description = form.cleaned_data.get('description')
            if deadline_at == '':
                deadline_at = None
            if description == '':
                description = 'Отсутстувет'
            new_aim = ToDoList.objects.create(aim=aim, status=status, deadline_at=deadline_at, description=description)
            return redirect('list_check', pk=new_aim.pk)
        return render(request, 'todolist_create.html', {'form': form})


def check_list_view(request, pk):
    try:
        check_list = ToDoList.objects.get(pk=pk)
    except ToDoList.DoesNotExist:
        return HttpResponseNotFound('Задача не найдена')
    context = {'aim_list': check_list}
    return render(request, 'check_list.html', context)


def update_list_view(request, pk):
    aim_list = get_object_or_404(ToDoList, pk=pk)
    if request.method == 'GET':
        form = ToDoListForm(initial={
            'aim': aim_list.aim,
            'description': aim_list.description,
            'status': aim_list.status,
            'deadline_at': aim_list.deadline_at
        })
        return render(request, 'updatelist.html', {'aim_list': aim_list, 'form':form})
    else:
        form = ToDoListForm(data=request.POST)
        if form.is_valid():
            aim_list.aim = form.cleaned_data.get('aim')
            aim_list.status = form.cleaned_data.get('status')
            aim_list.deadline_at = form.cleaned_data.get('deadline_at')
            aim_list.description = form.cleaned_data.get('description')
            if aim_list.deadline_at == '':
                aim_list.deadline_at = None
            if aim_list.description == '':
                aim_list.description = 'Отсутстувет'
            aim_list.save()
            return redirect('list_check', pk=aim_list.pk)
        return render(request, 'updatelist.html', {'aim_list': aim_list, 'form': form})


def delete_list_view(request, pk):
    aim_list = ToDoList.objects.get(pk=pk)
    if request.method == 'GET':
        return render(request, 'todolist_delete.html', {'aim_list': aim_list})
    else:
        aim_list.delete()
        return redirect('index')
