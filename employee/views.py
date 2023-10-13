from django.shortcuts import render,redirect

def home(request):
    return render(request,"employee/home.html")

def about(request):
    return render(request,"employee/about.html")

