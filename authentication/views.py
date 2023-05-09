from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import UserRegistrationForm
from scheduling.models import WorkShift

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # ...
            return redirect('authentication:login')
    else:
        form = UserRegistrationForm()
    return render(request, 'authentication/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        print(user)  # Add this line to check if the user is authenticated
        if user is not None:
            login(request, user)
            return redirect('profiles:profile_detail')
        else:
            error_message = 'Invalid username or password.'
            return render(request, 'authentication/login.html', {'error_message': error_message})
    else:
        return render(request, 'authentication/login.html')

def user_logout(request):
    logout(request)
    return redirect('authentication:login')
