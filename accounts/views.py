from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import SignUpForm, LoginForm
from .models import CustomUser
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib import messages

def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]

            # Create the user and set the raw password
            user = CustomUser(email=email)
            user.set_password(password)  # This will save both encrypted and raw passwords
            user.save()
            
            messages.success(request, "Account created successfully. Please log in.")
            return redirect("login")
    else:
        form = SignUpForm()
    return render(request, "signup.html", {"form": form})

def login_view(request):
    form = LoginForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect("home") 
            else:
                messages.error(request, "Invalid email or password")
    
    return render(request, "login.html", {"form": form})

@login_required
def home(request):
    return render(request, 'home.html')
