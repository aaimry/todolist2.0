from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views import View
from django.views.generic import TemplateView, FormView, ListView
from todolist.base import FormView as CustomFormView

from todolist.forms import ToDoListForm, SearchForm
from todolist.models import ToDoList


class IndexView(ListView):
    model = ToDoList
    context_object_name = "aim_list"
    template_name = "todolist.html"
    paginate_by = 10
    paginate_orphans = 0

    def get(self, request, *args, **kwargs):
        self.form = self.get_form()
        self.search_value = self.get_search_value()
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.search_value:
            query = Q(aim__icontains=self.search_value) | Q(description__icontains=self.search_value)
            queryset = queryset.filter(query)
        return queryset.order_by("-create_date")

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['form'] = SearchForm()
        if self.search_value:
            context['form'] = SearchForm(initial={"search": self.search_value})
            context['search'] = self.search_value
        return context

    def get_form(self):
        return SearchForm(self.request.GET)

    def get_search_value(self):
        if self.form.is_valid():
            return self.form.cleaned_data.get("search")


class CreateView(CustomFormView):
    form_class = ToDoListForm
    template_name = 'todolist_create.html'

    def form_valid(self, form):
        # type = form.cleaned_data.pop('type')
        # self.object = ToDoList.objects.create(**form.cleaned_data)
        # self.object.type.set(type)
        self.object = form.save()
        return super().form_valid(form)

    def get_redirect_url(self):
        return redirect('list_check', pk=self.object.pk)


class CheckListView(TemplateView):
    template_name = 'check_list.html'

    def get_context_data(self, **kwargs):
        check_list = ToDoList.objects.get(pk=kwargs.get('pk'))
        kwargs['check_list'] = check_list
        return super().get_context_data(**kwargs)


class UpdateView(FormView):
    form_class = ToDoListForm
    template_name = 'updatelist.html'

    def dispatch(self, request, *args, **kwargs):
        self.aim_list = self.get_object()
        return super(UpdateView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['aim_list'] = self.aim_list
        return context

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['instance'] = self.aim_list
        return kwargs

    def form_valid(self, form):
        self.aim_list = form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('list_check', kwargs={"pk": self.aim_list.pk})

    def get_object(self):
        return get_object_or_404(ToDoList, pk=self.kwargs.get("pk"))


class DeleteView(View):

    def get(self, request, *args, **kwargs):
        aim_list = get_object_or_404(ToDoList, pk=kwargs.get('pk'))
        return render(request, 'todolist_delete.html', {'aim_list': aim_list})

    def post(self, request, *args, **kwargs):
        aim_list = get_object_or_404(ToDoList, pk=kwargs.get('pk'))
        aim_list.delete()
        return redirect('index')
