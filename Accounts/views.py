from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse
from django.contrib import messages



def signUp_view(request):
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        confirmPassword=request.POST.get("confirmPassword")
        if password != confirmPassword:
           messages.warning(request,"Password & confirm Password must be same")
           return redirect("signUp")
        user=authenticate(request,username=username,password=password)
        if user is not None:
            messages.warning(request,"Account already exists")
            return redirect("signUp")
        user = User.objects.create_user(username=username,password=password)
        login(request,user)
        messages.success(request,"Account created successfully")
        return redirect("home")
    return render(request,"Accounts/signUpPage.html")



def  login_view(request):
     if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,"Logged in successfully")
            return redirect("home") 
        else:
            messages.error(request, "Invalid username or password")  
     return render(request,"Accounts/loginPage.html")



def logout_view(request):
    if  request.user:
        logout(request)
    messages.success(request,"Logged out successfully")
    return redirect("login")

