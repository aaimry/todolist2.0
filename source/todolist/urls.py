from django.urls import path
from todolist.views import todolist_view, create_todolist_view, check_list_view, update_list_view, delete_list_view

urlpatterns = [
    path('', todolist_view, name='index'),
    path('add/', create_todolist_view, name='list_add'),
    path('check/<int:pk>/', check_list_view, name='list_check'),
    path('check/<int:pk>/update', update_list_view, name='list_update'),
    path('check/<int:pk>/delete', delete_list_view, name='list_delete')
]
