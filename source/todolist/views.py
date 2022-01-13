from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import TemplateView

from todolist.forms import ToDoListForm
from todolist.models import ToDoList


class IndexView(View):
    def get(self, request):
        aim_list = ToDoList.objects.all()
        return render(request, 'todolist.html', {'aim_list': aim_list})


class CreateView(View):
    def get(self, request):
        form = ToDoListForm()
        return render(request, 'todolist_create.html', {'form': form})

    def post(self, request):
        form = ToDoListForm(data=request.POST)
        if form.is_valid():
            aim = form.cleaned_data.get('aim')
            status = form.cleaned_data.get('status')
            type = form.cleaned_data.get('type')
            description = form.cleaned_data.get('description')
            if description == '':
                description = 'Отсутстувет'
            new_aim = ToDoList.objects.create(aim=aim, description=description, type=type, status=status)
            return redirect('list_check', pk=new_aim.pk)
        return render(request, 'todolist_create.html', {'form': form})


class CheckListView(TemplateView):
    template_name = 'check_list.html'

    def get_context_data(self, **kwargs):
        check_list = ToDoList.objects.get(pk=kwargs.get('pk'))
        kwargs['check_list'] = check_list
        return super().get_context_data(**kwargs)


class UpdateView(View):
    def get(self, request, *args, **kwargs):
        aim_list = get_object_or_404(ToDoList, pk=kwargs.get('pk'))
        form = ToDoListForm(initial={
            'aim': aim_list.aim,
            'description': aim_list.description,
            'type': aim_list.type,
            'status': aim_list.status,
        })
        return render(request, 'updatelist.html', {'aim_list': aim_list, 'form': form})

    def post(self, request, *args, **kwargs):
        aim_list = get_object_or_404(ToDoList, pk=kwargs.get('pk'))
        form = ToDoListForm(data=request.POST)
        if form.is_valid():
            aim_list.aim = form.cleaned_data.get('aim')
            aim_list.status = form.cleaned_data.get('status')
            aim_list.type = form.cleaned_data.get('type')
            aim_list.description = form.cleaned_data.get('description')
            if aim_list.description == '':
                aim_list.description = 'Отсутстувет'
            aim_list.save()
            return redirect('list_check', pk=aim_list.pk)
        return render(request, 'updatelist.html', {'aim_list': aim_list, 'form': form})


class DeleteView(View):

    def get(self, request, *args, **kwargs):
        aim_list = get_object_or_404(ToDoList, pk=kwargs.get('pk'))
        return render(request, 'todolist_delete.html', {'aim_list': aim_list})

    def post(self, request, *args, **kwargs):
        aim_list = get_object_or_404(ToDoList, pk=kwargs.get('pk'))
        aim_list.delete()
        return redirect('index')
