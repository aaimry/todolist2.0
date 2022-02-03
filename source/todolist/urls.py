from django.urls import path
from todolist.views import (
    IndexView,
    TrackerCheckListView,
    TrackerDeleteView,
    TrackerUpdateView,
    TrackerCreateView, ProjectView, CheckProjectView, ProjectCreateView, DeleteProjectView, UpdateProjectView)

urlpatterns = [
    path('', ProjectView.as_view(), name='projects'),
    path('add/', ProjectCreateView.as_view(), name='projects_add'),
    path('check/<int:pk>', CheckProjectView.as_view(), name='projects_check'),
    path('check/<int:pk>/update', UpdateProjectView.as_view(), name='projects_update'),
    path('check/<int:pk>/delete', DeleteProjectView.as_view(), name='projects_delete'),
    path('projects/issues', IndexView.as_view(), name='index'),
    path('project/<int:pk>/add/', TrackerCreateView.as_view(), name='list_add'),
    path('project/check/<int:pk>/', TrackerCheckListView.as_view(), name='list_check'),
    path('project/check/<int:pk>/update', TrackerUpdateView.as_view(), name='list_update'),
    path('project/check/<int:pk>/delete', TrackerDeleteView.as_view(), name='list_delete'),
]
