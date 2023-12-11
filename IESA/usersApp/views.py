from django.contrib.auth import login, logout
from django.shortcuts import redirect

from .forms import CustomUserCreationForm, UserProfileForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import CustomUserCreationForm
from .forms import LoginForm


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()

            # Вручную аутентифицировать пользователя
            user.backend = 'django.contrib.auth.backends.ModelBackend'  # Указывает бэкенд аутентификации Django
            login(request, user)

            return redirect('home')
    else:
        form = CustomUserCreationForm()

    return render(request, 'usersApp/register.html', {'form': form})


def profile(request):
    user = request.user  # Получаем объект пользователя текущей сессии
    return render(request, 'usersApp/profile.html', {'user': user})


def edit_profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()  # Update the user's data
            return redirect('profile')  # Redirect to the user's profile page
    else:
        form = UserProfileForm(instance=request.user)

    return render(request, 'usersApp/edit_profile.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                # Redirect to a success page.
                return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'usersApp/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('profile')
