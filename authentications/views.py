from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .models import SignupModel
from .forms import LoginForm, SignupForm

# Create your views here.


def login_hendler(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            return redirect('home:index')
        else:
            form = LoginForm(request.GET)
        return render(request, 'login.html', {'form': form})
    else:
        form = LoginForm(request.GET)
    return render(request, 'login.html', {'form': form})


def signup_hendler(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            check_password = form.cleaned_data['check_password']

            if check_password == password:
                SignupModel.objects.create(
                    username = username,
                    email = email,
                    password = password
                )
            else:
                form = SignupForm(request.GET)
                return render(request, 'login.html', {'form': form})
            
            return redirect('auth:login')
        else:
            form = SignupForm(request.GET)
            return render(request, 'signup.html', {'form': form})
    else:
        form = SignupForm(request.GET)
    return render(request, 'signup.html', {'form': form})


def logout_hendler(request):
    print('User logged out')
    return render(request, 'login.html')
