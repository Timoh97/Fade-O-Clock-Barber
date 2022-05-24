from django.urls import path,include
from django.views.generic.base import TemplateView
from . import views
urlpatterns = [
path('index/', views.index, name="index"),
path('about/', views.about, name="about"),
path('contact/', views.contact, name="contact"),
path('pricing/', views.pricing, name="pricing"),
path('services/', views.services, name="services"),

#registration
path('activate/complete/',
        TemplateView.as_view(
            template_name='registration/activation_complete.html'
        ),
        name='registration_activation_complete'),
    # The activation key can make use of any character from the
    # URL-safe base64 alphabet, plus the colon as a separator.
path('activate/(?P<activation_key>[-:\w]+)/',
        views.ActivationView.as_view(),
        name='registration_activate'),
path('register/',
        views.RegistrationView.as_view(),
        name='registration_register'),
path(r'register/complete/',
        TemplateView.as_view(
            template_name='registration/registration_complete.html'
        ),
        name='registration_complete'),
path('register/closed/',
        TemplateView.as_view(
            template_name='registration/registration_closed.html'
        ),
        name='registration_disallowed'),
path(r'', include('registration.auth_urls'))
]