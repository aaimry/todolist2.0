from django.urls import reverse
from django.views.generic import CreateView, DetailView, ListView
from django.shortcuts import get_object_or_404

from todolist.forms import ProjectsForm
from todolist.models import Projects, ToDoList


class ProjectView(ListView):
    model = Projects
    context_object_name = "projects"
    template_name = 'projects/projects.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset


class ProjectCreateView(CreateView):
    model = Projects
    form_class = ProjectsForm
    template_name = 'projects/create.html'

    def get_success_url(self):
        return reverse('projects_check', kwargs={'pk': self.object.pk})


class CheckProjectView(DetailView):
    template_name = 'projects/check.html'
    model = Projects

    def get_context_data(self, **kwargs):
        print(kwargs)
        context = super().get_context_data(**kwargs)
        check_project = get_object_or_404(Projects, pk=kwargs.get('object').id)
        context['check_project'] = check_project
        return context