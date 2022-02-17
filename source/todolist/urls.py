from django.urls import path
from .views import (
    IndexView,
    TrackerCheckListView,
    TrackerDeleteView,
    TrackerUpdateView,
    TrackerCreateView, ProjectView, CheckProjectView, ProjectCreateView, DeleteProjectView, UpdateProjectView,
    UserInProjectView,
)

app_name = 'tracker'

urlpatterns = [
    path('', ProjectView.as_view(), name='index_project'),
    path('add/', ProjectCreateView.as_view(), name='project_add'),
    path('check/<int:pk>', CheckProjectView.as_view(), name='project_check'),
    path('check/<int:pk>/update', UpdateProjectView.as_view(), name='project_update'),
    path('check/<int:pk>/delete', DeleteProjectView.as_view(), name='project_delete'),
    path('projects/issues', IndexView.as_view(), name='index'),
    path('project/<int:pk>/add/', TrackerCreateView.as_view(), name='list_add'),
    path('project/check/<int:pk>/', TrackerCheckListView.as_view(), name='list_check'),
    path('project/check/<int:pk>/update', TrackerUpdateView.as_view(), name='list_update'),
    path('project/check/<int:pk>/delete', TrackerDeleteView.as_view(), name='list_delete'),
    path('project/<int:pk>/user/update', UserInProjectView.as_view(), name='user_update')
]
