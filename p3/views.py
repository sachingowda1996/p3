from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,"first.html")

def home(request):
    return render(request,"first.html")

def second(request):
    return render(request,"directory/second.html") 

def third(request):
    return render(request,"directory/third.html",context={'data':"sachin",'name':"nagesh"}) 

def fourth(request):
    fruits=['strawberry','cherry','mango']
    return render(request,"directory/fourth.html",{'fruits':fruits}) 

def fifth(request):
    return render(request,"directory/fifth.html",{'a':10,'b':100})

def urls_data(request,name):
    return HttpResponse("<h1>{}</h1>".format(name))

def ab(request,a,b):
    sum=int(a)+int(b)
    return HttpResponse(str(sum))

def great_2_number(request,a,b):
    if a>b:
        return HttpResponse("the greatest value is {}".format(a))
    elif b>a:
        return HttpResponse("the greatest value is {}".format(b))
    else:
        return HttpResponse("all are equal")

def reverse(request,a):
    b=''
    for i in a:
        b=i+b
    return HttpResponse(str(b)) 
    
