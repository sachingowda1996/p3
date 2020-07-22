from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,"first.html")

def home(request):
    return render(request,"first.html")

def second(request):
    return render(request,"directory/second.html")    
