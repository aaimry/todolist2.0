from django.urls import path
from todolist.views import IndexView, CheckListView, DeleteView, UpdateView, CreateView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('add/', CreateView.as_view(), name='list_add'),
    path('check/<int:pk>/', CheckListView.as_view(), name='list_check'),
    path('check/<int:pk>/update', UpdateView.as_view(), name='list_update'),
    path('check/<int:pk>/delete', DeleteView.as_view(), name='list_delete')
]
