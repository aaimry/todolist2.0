from django.urls import path
from todolist.views import (
    IndexView,
    CheckListView,
    DeleteView,
    UpdateView,
    IssuesCreateView, ProjectView, CheckProjectView, ProjectCreateView)

urlpatterns = [
    path('', ProjectView.as_view(), name='projects'),
    path('add/', ProjectCreateView.as_view(), name='projects_add'),
    path('check/<int:pk>', CheckProjectView.as_view(), name='projects_check'),
    path('projects/issues', IndexView.as_view(), name='index'),
    path('project/<int:pk>/add/', IssuesCreateView.as_view(), name='list_add'),
    path('project/check/<int:pk>/', CheckListView.as_view(), name='list_check'),
    path('project/check/<int:pk>/update', UpdateView.as_view(), name='list_update'),
    path('project/check/<int:pk>/delete', DeleteView.as_view(), name='list_delete'),
]
