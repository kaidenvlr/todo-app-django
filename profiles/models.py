from django.contrib.auth.models import User
from django.db import models

COLOR_PALETTE = [
    ("#C70039", "red"),
    ("#0096FF", "blue"),
    ("#FFFFFF", "white"),
    ("#848484", "gray"),
    ("#6A00DF", "purple"),
    ("#00A131", "green"),
    ("#FFC300", "yellow"),
]


class ProfileCategory(models.Model):
    profile = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    name = models.CharField(max_length=200, verbose_name='Название списка заданий')
    color = models.CharField(max_length=7, verbose_name='Цвет списка', choices=COLOR_PALETTE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} - {self.profile.username}"

    class Meta:
        verbose_name = "Список задач пользователя"
        verbose_name_plural = "Списки задач пользователей"
        order_with_respect_to = 'profile'
