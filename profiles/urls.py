from django.urls import path, include

from profiles import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('register', views.register_view, name='register'),

    path('create-list', views.create_list_view, name='create-list'),
    path('list&task=<int:pk>', views.list_view, name='list'),
    path('list&task=<int:pk>/edit', views.edit_list_view, name='edit-list'),
    path('list&task=<int:pk>/delete', views.delete_task_list_view, name='delete-list'),
]
