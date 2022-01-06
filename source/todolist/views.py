from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponseNotFound

from forms import ToDoListForm
from todolist.models import ToDoList
from django.urls import reverse


def todolist_view(request):
    aim_list = ToDoList.objects.all()
    return render(request, 'todolist.html', {'aim_list': aim_list})


def create_todolist_view(request):
    if request.method == 'GET':
        context = {'status': ToDoList.status_choices}
        return render(request, 'todolist_create.html', context)
    else:
        aim = request.POST.get('aim')
        status = request.POST.get('status')
        deadline_at = request.POST.get('deadline_at')
        description = request.POST.get('description')
        if deadline_at == '':
            deadline_at = None
        if description == '':
            description = 'Отсутстувет'
        new_aim = ToDoList.objects.create(aim=aim, status=status, deadline_at=deadline_at, description=description)
        return redirect('list_check', pk=new_aim.pk)


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
        return render(request, 'updatelist.html', {'aim_list': aim_list})
    else:
        aim_list.aim = request.POST.get('aim')
        aim_list.status = request.POST.get('status')
        aim_list.deadline_at = request.POST.get('deadline_at')
        aim_list.description = request.POST.get('description')
        aim_list.save()
        return redirect('check_list_view', pk=aim_list.pk)


def delete_list_view(request, pk):
    aim_list = ToDoList.objects.get(pk=pk)
    if request.method == 'GET':
        return render(request, 'todolist_delete.html', {'aim_list': aim_list})
    else:
        aim_list.delete()
        return redirect('index')


