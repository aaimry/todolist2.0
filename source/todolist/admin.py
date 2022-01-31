from django.contrib import admin


from todolist.models import ToDoList, StatusChoice, TypeChoice, Projects


class ToDoListAdmin(admin.ModelAdmin):
    list_display = ['id', 'project', 'aim', 'status']
    list_filter = ['aim']
    search_fields = ['aim', 'status']
    fields = [ 'aim', 'description',  'status', 'type']


admin.site.register(ToDoList, ToDoListAdmin)


class StatusChoiceAdmin(admin.ModelAdmin):
    list_display = ['id', 'status_obj']
    list_filter = ['status_obj']
    search_fields = ['status_obj']
    fields = ['status_obj']


admin.site.register(StatusChoice, StatusChoiceAdmin)


class TypeChoiceAdmin(admin.ModelAdmin):
    list_display = ['id', 'type_obj']
    list_filter = ['type_obj']
    search_fields = ['type_obj']
    fields = ['type_obj']


admin.site.register(TypeChoice, TypeChoiceAdmin)


class ProjectsAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    list_filter = ['title']
    search_fields = ['title']
    fields = ['title', 'description', 'start_date', 'end_date']


admin.site.register(Projects, ProjectsAdmin)
