from django.db import models

from profiles.models import ProfileCategory


class TaskLevel(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название уровня задания')
    color = models.CharField(max_length=200, verbose_name='Цвет уровня задания')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Уровень заданий'
        verbose_name_plural = 'Уровни заданий'


class Task(models.Model):
    task_list = models.ForeignKey(ProfileCategory, on_delete=models.CASCADE, verbose_name='Список заданий')
    name = models.CharField(max_length=200, verbose_name='Название задания')
    level = models.ForeignKey(TaskLevel, on_delete=models.CASCADE, verbose_name='Уровень важности')
    is_done = models.BooleanField(default=False, verbose_name='Завершен?')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Задание'
        verbose_name_plural = 'Задания'
        order_with_respect_to = 'is_done'
