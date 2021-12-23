from django.shortcuts import render
from todolist.models import ToDoList


def todolist_view(request):
    aim_list = ToDoList.objects.all()
    return render(request, 'todolist.html', {'aim_list': aim_list})


def create_todolist_view(request):
    if request.method == 'GET':
        return render(request, 'todolist_create.html')
    else:
        aim = request.POST.get('aim')
        status = request.POST.get('status')
        deadline_at = request.POST.get('deadline_at')
        if deadline_at == '':
            deadline_at = None
        new_aim = ToDoList.objects.create(aim=aim, status=status, deadline_at=deadline_at)
        context = {"aim_list": new_aim}
        return render(request, 'todolist_create.html', context)