from django.shortcuts import render

from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.sites.shortcuts import get_current_site
from django.core import signing
from django.template.loader import render_to_string
from django.core.mail import send_mail
#registration imports
from django.http import HttpResponse  
from django.shortcuts import render, redirect  
from django.contrib.auth import login, authenticate  
from .forms import *
from django.contrib.sites.shortcuts import get_current_site  
from django.utils.encoding import force_bytes, force_text  
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode  
from django.template.loader import render_to_string  
from .token import account_activation_token  
from django.contrib.auth.models import User  
from django.core.mail import EmailMessage  
from django.contrib import messages

from django.utils import timezone

#displaying appointment
from django.urls import reverse_lazy

from .models import *
from bootstrap_modal_forms.generic import BSModalCreateView



# Create your views here.

def index(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("index")
    form=AppointmentForm()
    
    return render(request,'index.html',context={'form':form})

def about(request):
    
    return render(request,'about.html')


def contact(request):
    
    return render(request,'contact.html')

def pricing(request):
    
    return render(request,'pricing.html')

def services(request):
    
    return render(request,'services.html')
def profile(request):
    current_user = request.user
    profile = Profile.objects.filter(user_id=current_user.id).first()
    appointment = Appointment.objects.filter(user_id=current_user.id).first()
    return render(request,'profile.html',{'profile':profile,'appointment':appointment})

def appointment(request):
     if request.method == 'POST':
        form = AppointmentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("index")
     form=AppointmentForm()
     return render(request, 'appointment.html',context={'form':form})
    

def styles(request):
    
    return render(request,'styles.html')




#registration

def signup(request):  
    if request.method == 'POST':  
        form = SignupForm(request.POST)  
        if form.is_valid():  
            # save form in the memory not in database  
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            email = form.cleaned_data['email']
            user = authenticate(username=username, password=raw_password) 
            login(request,user)
            # subject = 'Welcome to the EQUINOX!'
            # message = f'Hi {user.username},\nWe officially welcome you to our growing community.See how you would like to shave, and contact us.\nRemember to enjoy the app!\n\nKind Regards,\nThe Management.'
            # email_from = settings.EMAIL_HOST_USER
            # email=email
            # recepient_list = [user.email]
            # send_mail(subject,message,email_from,recepient_list)
            messages.success(request, 'Account created successfully! Check your email for a welcome mail')
            # to get the domain of the current site  
            current_site = get_current_site(request)  
            # mail_subject = 'Activation link has been sent to your email id'  
            # message = render_to_string('acc_active_email.html', {  
            #     'user': user,  
            #     'domain': current_site.domain,  
            #     'uid':urlsafe_base64_encode(force_bytes(user.pk)),  
            #     'token':account_activation_token.make_token(user),  
            # })  
            # to_email = form.cleaned_data.get('email')  
            # email = EmailMessage(  
            #             mail_subject, message, to=[to_email]  
            # )  
            # email.send()  
            # return HttpResponse('Please confirm your email address to complete the registration') 
        return redirect('/login') 
    else:  
        form = SignupForm()  
    return render(request, 'signup.html', {'form': form}) 


def loginView(request):
	if request.method == "POST":
		form = LoginForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("/index")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = LoginForm()
	return render(request=request, template_name="login.html", context= {"form":form})

#create activation view
def activate(request, uidb64, token):  
    User = get_user_model()  
    try:  
        uid = force_text(urlsafe_base64_decode(uidb64))  
        user = User.objects.get(pk=uid)  
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):  
        user = None  
    if user is not None and account_activation_token.check_token(user, token):  
        user.is_active = True  
        user.last_login = timezone.now()
        user.save()  
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')  
    else:  
        return HttpResponse(request,'Activation link is invalid!') 