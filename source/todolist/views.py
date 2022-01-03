from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponseNotFound
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
            description = None
        new_aim = ToDoList.objects.create(aim=aim, status=status, deadline_at=deadline_at, description=description)
        return redirect('list_check', pk=new_aim.pk)


def check_list_view(request, pk):
    try:
        check_list = ToDoList.objects.get(pk=pk)
    except ToDoList.DoesNotExist:
        return HttpResponseNotFound('Задача не найдена')
    context = {'aim_list': check_list}
    return render(request, 'check_list.html', context)