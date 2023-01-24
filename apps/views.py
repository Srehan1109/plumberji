from django.shortcuts import render
from .models import Service
# Create your views here.

def carts(request):
    return render(request,'apps/carts.html')


# def all_service(request):
#     service = Service.objects.all()
#     print(service)
#     context = {
#         'service' : service
#     }
#     return render(request,'plumberji/home.html',context)