from django.shortcuts import render


def todolist_view(request):
    return render(request, 'todolist.html')