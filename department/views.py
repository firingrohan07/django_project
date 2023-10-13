from django.shortcuts import render,redirect

def home(request):
    return render(request,"department/home.html")

def about(request):
    return render(request,"department/about.html")

