from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# SIGNUP
def signup_view(request):
    error = None

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():
            error = "Username already exists!"
        else:
            User.objects.create_user(username=username, password=password)
            return redirect('login')

    return render(request, 'signup.html', {'error': error})


# LOGIN
def login_view(request):
    error = None

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            error = "Invalid username or password"

    return render(request, 'login.html', {'error': error})


# LOGOUT
def logout_view(request):
    logout(request)
    return redirect('login')