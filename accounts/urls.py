from django.urls import path
from . import views

name = 'accounts'

urlpatterns = [
    path("login", views.login, name='login'),
    path("register", views.register, name='register'),
    path('logout/',views.logout,name="logout"),
    path('activate/<uidb64>/<token>/',views.activate,name="activate"),
    path('forgotpassword/',views.forgotpassword,name="forgotpassword"),
    path('resetpassword_validate/<uidb64>/<token>/',views.resetpassword_validate,name="resetpassword_validate"),
    path('resetpassword/',views.resetpassword,name="resetpassword"),
    path("plumberlogin", views.plumberlogin, name='plumberlogin'),
    path("plumberregister", views.plumberregister, name='plumberregister'),
    path('plumberactivate/<uidb64>/<token>/',views.plumberactivate,name="plumberactivate"),
]
