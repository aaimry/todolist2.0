from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from todolist.forms import ToDoListForm, SearchForm
from todolist.models import ToDoList, Projects


class IndexView(LoginRequiredMixin, ListView):
    model = ToDoList
    context_object_name = "aim_list"
    template_name = "tracker/todolist.html"
    paginate_by = 8
    paginate_orphans = 0

    def get(self, request, *args, **kwargs):
        self.form = self.get_form()
        self.search_value = self.get_search_value()
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.search_value:
            print(self.search_value)
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


class TrackerCreateView(PermissionRequiredMixin, CreateView):
    model = ToDoList
    form_class = ToDoListForm
    template_name = 'tracker/todolist_create.html'
    permission_required = "todolist.add_todolist"

    def has_permission(self):
        project = get_object_or_404(Projects, id=self.kwargs.get('pk'))
        return super().has_permission() and (self.request.user in project.user.all())

    def form_valid(self, form):
        project = get_object_or_404(Projects, id=self.kwargs.get('pk'))
        self.todolist = form.save(commit=False)
        self.todolist.project = project
        self.todolist.save()
        form.save_m2m()
        return self.get_success_url()

    def get_success_url(self):
        return redirect('tracker:list_check', pk=self.todolist.id)


class TrackerCheckListView(DetailView):
    template_name = 'tracker/check_list.html'
    model = ToDoList

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        check_list = get_object_or_404(ToDoList, pk=kwargs.get('object').id)
        context['check_list'] = check_list
        return context


class TrackerUpdateView(PermissionRequiredMixin, UpdateView):
    form_class = ToDoListForm
    template_name = "tracker/updatelist.html"
    model = ToDoList
    context_object_name = 'aim_list'
    permission_required = "todolist.change_todolist"

    def has_permission(self):
        todolist = get_object_or_404(ToDoList, pk=self.kwargs.get('pk'))
        return super().has_permission() and self.request.user in todolist.project.user.all()

    def get_success_url(self):
        return reverse('tracker:project_check', kwargs={'pk': self.object.project.pk})


class TrackerDeleteView(PermissionRequiredMixin, DeleteView):
    model = ToDoList
    template_name = "tracker/todolist_delete.html"
    context_object_name = 'aim_list'
    permission_required = "todolist.delete_todolist"

    def has_permission(self):
        todolist = get_object_or_404(ToDoList, id=self.kwargs.get('pk'))
        return super().has_permission() and self.request.user in todolist.project.user.all()

    def get_success_url(self):
        return reverse('tracker:project_check', kwargs={'pk': self.object.project.pk})