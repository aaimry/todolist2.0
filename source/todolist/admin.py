from django.contrib import admin

# Register your models here.
from todolist.models import ToDoList


class ToDoListAdmin(admin.ModelAdmin):
    list_display = ['id', 'aim', 'status', 'deadline_at']
    list_filter = ['aim']
    search_fields = ['aim', 'status']
    fields = ['aim', 'status', 'description', 'deadline_at']


admin.site.register(ToDoList, ToDoListAdmin)