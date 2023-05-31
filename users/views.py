from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm
from .models import Profiles


def login_page(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('profiles')

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'Username does not exist')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('profiles')
        else:
            messages.error(request, 'Username or Password are incorrect')
    return render(request, 'users/login_register.html')


def logout_user(request):
    logout(request)
    messages.info(request, 'User was successfully logged out')
    return redirect('login')


def register_user(request):
    page = 'register'
    form = CustomUserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, 'Account created successfully')
            login(request, user)
            return redirect('profiles')
        else:
            messages.error(request, 'An error occured during registration')

    context = {'page':page, 'form':form}
    return render(request, 'users/login_register.html', context)

# Profile page
def profiles(request):
    profiles = Profiles.objects.all()
    context = {'profiles': profiles}
    return render(request, 'users/profiles.html', context)

def profile(request, username):
    profile = Profiles.objects.get(username=username)
    topskills = profile.skill_set.exclude(description__exact="")
    otherskills = profile.skill_set.filter(description="")
    context = {'profile': profile, 'topskills': topskills, 'otherskills': otherskills}
    return render(request, 'users/profile.html', context)
