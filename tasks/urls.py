from django.urls import path

from tasks import views

urlpatterns = [
    path('list&task=<int:pk>/create-task', views.create_task_view, name="create-task"),
    path('list&task=<int:pk>?id=<int:task_id>/delete', views.delete_task_view, name='delete-task'),
    path('list&task=<int:pk>?id=<int:task_id>/complete', views.complete_task_view, name='complete-task'),
    path('list&task=<int:pk>?id=<int:task_id>/incomplete', views.incomplete_task_view, name='incomplete-task'),
]
