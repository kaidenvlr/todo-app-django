from django.urls import path, include

from profiles import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('register', views.register_view, name='register'),

    path('create-list', views.create_list_view, name='create-list'),
]
