from django.shortcuts import render

from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.sites.shortcuts import get_current_site
from django.core import signing
from django.template.loader import render_to_string





# Create your views here.

def index(request):

        
    return render(request,'index.html')


def contact(request):
    return('contact.html',request)

def pricing (request):
    return('pricing.html',request)

def services (request):
    return(request,'services.html')

def about (request):
    return('about.html',request)


