from django.contrib import admin
from tasks import models


@admin.register(models.TaskLevel)
class TaskLevelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'color')


@admin.register(models.Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'task_list', 'level', 'name', 'is_done', 'updated_at')
