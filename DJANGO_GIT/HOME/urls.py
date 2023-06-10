from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="Home page"),
    path('about/', views.about, name="About"),
    path('contacts/', views.contacts, name="Contacts"),
    path('services/', views.services, name="Services")
]