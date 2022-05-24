from django.urls import path,include
from . import views
urlpatterns = [
path('', views.index, name="index"),
path('', views.about, name="index"),
path('', views.contact, name="index"),
path('', views.pricing, name="index"),
path('', views.services, name="index"),
]