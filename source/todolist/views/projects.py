from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse
from django.views.generic import CreateView, DetailView, ListView, DeleteView, UpdateView
from django.shortcuts import get_object_or_404

from todolist.forms import ProjectsForm, ProjectUserForm
from todolist.models import Projects


class ProjectView(ListView):
    model = Projects
    context_object_name = "projects"
    template_name = 'projects/projects.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset


class ProjectCreateView(PermissionRequiredMixin, CreateView):
    model = Projects
    form_class = ProjectsForm
    template_name = 'projects/create.html'
    permission_required = "todolist.add_projects"

    def form_valid(self, form):
        self.object = form.save()
        self.object.user.set([self.request.user])
        self.object.save()
        return super().form_valid(form)

    def has_permission(self):
        return super().has_permission()

    def get_success_url(self):
        return reverse('tracker:project_check', kwargs={'pk': self.object.pk})


class CheckProjectView(DetailView):
    template_name = 'projects/check.html'
    model = Projects

    def get_context_data(self, **kwargs):
        print(kwargs)
        context = super().get_context_data(**kwargs)
        check_project = get_object_or_404(Projects, pk=kwargs.get('object').id)
        context['check_project'] = check_project
        return context


class UpdateProjectView(PermissionRequiredMixin, UpdateView):
    form_class = ProjectsForm
    template_name = "projects/update.html"
    model = Projects
    permission_required = "todolist.change_projects"

    def has_permission(self):
        return super().has_permission() and self.request.user in self.get_object().user.all()

    def get_success_url(self):
        return reverse('tracker:index_project')


class DeleteProjectView(PermissionRequiredMixin, DeleteView):
    model = Projects
    permission_required = "todolist.delete_projects"

    def has_permission(self):
        return super().has_permission() and self.request.user in self.get_object().user.all()

    def get(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('tracker:index_project')


class UserInProjectView(PermissionRequiredMixin, UpdateView):
    permission_required = 'auth.add_user'
    form_class = ProjectUserForm
    model = Projects
    template_name = 'user/update.html'
    context_object_name = 'project'

    def has_permission(self):
        return super().has_permission() and self.request.user in self.get_object().user.all()

    def get_form(self, form_class=None):
        if form_class is None:
            form_class = self.get_form_class()
        return form_class(self.request, **self.get_form_kwargs())

    def get_success_url(self):
        return reverse('tracker:project_check', kwargs={'pk': self.object.get('pk')})
