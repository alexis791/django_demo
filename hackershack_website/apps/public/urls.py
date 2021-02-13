from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

app_name="public"

urlpatterns = [
    path('', views.index, name="index"),
    path('about', views.about, name="about"),
    path('contact', views.contact, name="contact")
]