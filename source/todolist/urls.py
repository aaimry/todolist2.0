from django.urls import path
from todolist.views import todolist_view, create_todolist_view

urlpatterns = [
    path('', todolist_view),
    path('add/', create_todolist_view)
    ]