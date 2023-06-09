# Generated by Django 4.1.7 on 2023-03-12 15:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
            },
        ),
        migrations.CreateModel(
            name='ProfileCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Название списка заданий')),
                ('color', models.CharField(choices=[('red', '#C70039'), ('blue', '#0096FF'), ('white', '#FFFFFF'), ('gray', '#848484'), ('purple', '#6A00DF'), ('green', '#00A131'), ('yellow', '#FFC300')], max_length=7, verbose_name='Цвет списка')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.profile')),
            ],
            options={
                'verbose_name': 'Список задач пользователя',
                'verbose_name_plural': 'Списки задач пользователей',
            },
        ),
    ]
