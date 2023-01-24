from http import client
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, redirect
from .forms import EnquiryForm
from django.core.mail import send_mail
from . models import Enquiry
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode,urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.core.mail import EmailMessage
from django.contrib.auth.tokens import default_token_generator
from apps.models import Service
#sms

from twilio.rest import Client


def home(request):
    service = Service.objects.all()
    print(service)
    context = {
        'service' : service
    }
    return render(request,'plumberji/home.html',context)

def something(request):
    if request.method == 'POST':
        form = EnquiryForm(request.POST)
        print(form.errors)
        if form.is_valid():

            form.save()
            #print(form)
            # email_fetched=Enquiry.objects.get(email=form.email)
            email_user = form.data['email']
            #print(email_user)
            sms_user= form.data['contact_number']
            #print(sms_user)
            job_to_be_done= form.data['job_to_be_done']
            #print(job_to_be_done)
            current_site=get_current_site(request)
            mail_subject="Email from Plumberji"
            messages="Hii Your Complain have register"
          
            to_email=email_user
            send_mail=EmailMessage(mail_subject,messages,to=[to_email])
            send_mail.send()  
            print('_______fhtshtshstr')
            #sms feature
            acc_id="AC13a27bfe95d8a0020859a9f9804be6a5"
            auth_token="530970117df22c46dc2697bf22170dab"
            sms = Client(acc_id,auth_token)
            sms_sender = sms.messages.create(
                                    body="hii this is your appointment",
                                    from_= "+16187597644",
                                    to="+917715055898",
                                )
            print('===============',sms_sender)
            print("message sent successfully")       
            return redirect('register')

        return redirect("home")
    else:
        form=EnquiryForm()

    context = {'form': form}
    template = 'apps/something.html'
    return render(request,template, context)


def about(request):
    template = 'plumberji/about.html'
    return render(request, template, {})


def contact(request):
    template = 'plumberji/contact.html'
    return render(request, template, {})


def support(request):
    template = 'plumberji/support.html'
    return render(request, template, {})


def faqs(request):
    template = 'plumberji/faqs.html'
    return render(request, template, {})
