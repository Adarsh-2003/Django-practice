from django.shortcuts import render,HttpResponse

# Create your views here.

def index(request):
    return render(request,'index.html')
    # return HttpResponse("This is homepage")

def about(request):
    return HttpResponse("This is about")

def services(request):
    return HttpResponse("This is services")

def contact(request):
    return HttpResponse("This is contact")
