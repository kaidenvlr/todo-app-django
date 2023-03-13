from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from profiles.forms import RegisterUserForm, ListCreateForm
from profiles.models import ProfileCategory


def home(request):
    if not request.user.is_authenticated:
        return render(request, "index.html")
    profile = User.objects.get(username=request.user.username)
    profile_lists = ProfileCategory.objects.filter(profile=profile)
    return render(request, "index.html", {'lists': profile_lists})


def register_view(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ("Registration Successful",))
            return redirect('home')
    else:
        form = RegisterUserForm
    return render(request, 'profiles/register.html', {'form': form})


def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.success(request, ("There Was An Error Loggin In, Try Again"))
            return redirect('home')
    else:
        return render(request, 'profiles/login.html', {})


def logout_view(request):
    logout(request)
    messages.success(request, ("Successfully logged out",))
    return redirect('home')


def create_list_view(request):
    if request.method == "POST":
        form = ListCreateForm(request.POST)
        if form.is_valid():
            task_list = form.save(commit=False)
            task_list.profile = request.user
            task_list.save()
            return redirect('home')
    else:
        form = ListCreateForm()
    return render(request, 'tasks/create-task-list.html', {'form': form})
