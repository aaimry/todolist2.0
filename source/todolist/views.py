from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from todolist.models import ToDoList
from django.urls import reverse

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
        # url = reverse('list_check', kwargs={'pk': new_aim.pk})
        # return HttpResponseRedirect(url)
        return redirect('list_check', pk=new_aim.pk)


def check_list_view(request, pk):
    # pk = request.GET.get('pk')
    check_list = ToDoList.objects.get(pk=pk)
    context = {'aim_list': check_list}
    return render(request, 'check_list.html', context)