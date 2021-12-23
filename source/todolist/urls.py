from django.urls import path
from todolist.views import todolist_view

urlpatterns = [
    path('/', todolist_view)
    ]