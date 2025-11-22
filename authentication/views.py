from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .forms import RegistrationForm
from django.contrib.auth.decorators import login_required

def landing_view(request):
    return render(request, 'auth/landing_page.html')

def register_user(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request,"Account created")
            return redirect('login')
        else:
            messages.error(request,"You have an error, Please check the error below!")

    else:
        form = RegistrationForm()

    return render(request, "auth/register.html", {"form": form})

def login_user(request):
     if request.method == "POST":
        form = AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")

            user = authenticate(username=username,password=password)
            if user is not None:
                login(request, user)
                messages.success(request,f"Welcome back, {username}!")
                return redirect('dashboard')

            else:
                messages.error(request," No  username or password matched")
                return redirect('login')
        else:
            messages.error(request,"No  username or password matched")
            return redirect('login')

     else:
        form = AuthenticationForm()

        return render(request, "auth/login.html", {"form": form})

def logout_user(request):
    logout(request)
    messages.info(request, "You have been logout")
    return redirect("landing_page")

