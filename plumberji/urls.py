from django.urls import path
from . import views

name = 'plumberji'

urlpatterns = [
    path("", views.home, name='home'),
    path("about/", views.about, name='about'),
    path("contact/", views.contact, name='contact'),
    path("support/", views.support, name='support'),
    path("faqs/", views.faqs, name='faqs'),
]
