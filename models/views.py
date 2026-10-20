from django.shortcuts import render
from .models import Profile
from django.contrib.auth.models import User
from django.contrib import messages 
from django.shortcuts import redirect


# this app will be for the accounts and for the model for persinalization

def register(request):
    if request.method=="POST":
        username=request.POST.get("username")
        email=request.POST.get("email")
        password=request.POST.get("password")

        if User.objects.filter(username=username).exists():
            messages.error(request,"Username already taken")
            return redirect('register')

        if User.objects.filter(email=email).exists():
            messages.error(request,"Email already in use")
            return redirect('register')

        user=User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        Profile.objects.create(
            user=user
        )

        return redirect('home')
    
    return render(request,'register.html')

def login(request):
    return render(request,'login.html')

def profile(request):
    profile=Profile.objects.get(user=request.user)
    movies=profile.watched.all()
    return render(request,'profile.html',{'movies':movies})