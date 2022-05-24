from django.shortcuts import render

# Create your views here.

def index(request):

        
    return render(request,'index.html')


def contact(request):
    return('contact.html',request)

def pricing (request):
    return('pricing.html',request)

def services (request):
    return('services.html',request)

def about (request):
    return('about.html',request)