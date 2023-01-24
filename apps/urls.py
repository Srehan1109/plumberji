from django.urls import path
from . import views


urlpatterns = [
    path('carts/', views.carts, name='carts'),
    # path('all_service/', views.all_service, name='all_service')
]