from django.contrib import admin
from . import models
from django.db.models import Count

# Register your models here.

admin.site.register(models.Category)

@admin.register(models.Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'status', 'user', 'category', 'created_at']
    list_per_page = 20
    list_editable = ['status']
    list_select_related = ['category', 'user']

    def tasks_count(self, object):
        return object.tasks_count
    
    def get_queryset(self, request):
        query = super().get_queryset(request) 
        query = query.annotate(task_count=Count('task'))
        return query
    
@admin.register(models.Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'description', 'project', 'is_completed']
    list_editable = ['is_completed']
    list_per_page = 20