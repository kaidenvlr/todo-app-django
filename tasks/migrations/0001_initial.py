# Generated by Django 4.1.7 on 2023-03-13 09:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('profiles', '0002_alter_profilecategory_color_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='TaskLevel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Название уровня задания')),
                ('color', models.CharField(max_length=200, verbose_name='Цвет уровня задания')),
            ],
            options={
                'verbose_name': 'Уровень заданий',
                'verbose_name_plural': 'Уровни заданий',
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Название задания')),
                ('is_done', models.BooleanField(default=False, verbose_name='Завершен?')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
                ('level', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasks.tasklevel', verbose_name='Уровень важности')),
                ('task_list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.profilecategory', verbose_name='Список заданий')),
            ],
            options={
                'verbose_name': 'Задание',
                'verbose_name_plural': 'Задания',
                'order_with_respect_to': 'is_done',
            },
        ),
    ]
