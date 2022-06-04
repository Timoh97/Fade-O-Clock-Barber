from django.urls import path,include
from django.views.generic.base import TemplateView
from . import views
from . views import activate
urlpatterns = [
path('index/', views.index, name="index"),
path('about/', views.about, name="about"),
path('contact/', views.contact, name="contact"),
path('appointment/', views.appointment, name="appointment"),
path('pricing/', views.pricing, name="pricing"),
path('profile/', views.profile, name="profile"),
path('styles/', views.styles, name="styles"),
path('services/', views.services, name="services"),
path('', views.signup, name="signup"),
path('login/', views.loginView, name="login"),

#registration
path('activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/',  
        activate, name='activate')
]