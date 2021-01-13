from django.shortcuts import render

def base(request):
    return render(request,'base.html')

def home(request):
    return render(request,'home.html')

def login(request):
    return render(request,'login.html')

def register(request):
    return render(request,'register.html')

def attendance(request):
    return render(request,'attendance.html')

def show_attnd(request):
    return render(request,'view_attnd.html')