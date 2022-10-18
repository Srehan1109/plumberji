
from django.shortcuts import get_object_or_404, render,redirect
from .forms import PlumberProfileFrom, RegistrationForm, UserProfileForm,UserForm
from .models import Account,UserProfile,PlumberProfile,Role
from django.contrib import messages,auth
from django.contrib.auth.decorators import login_required
import csv
from django.http import HttpResponse
#email activation imports
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode,urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.core.mail import EmailMessage
from django.contrib.auth.tokens import default_token_generator
 
# Create your views here.
def register(request):
    if request.method=='POST':
        form=RegistrationForm(request.POST)
        if form.is_valid():
            first_name=form.cleaned_data['first_name']
            last_name=form.cleaned_data['last_name']
            email=form.cleaned_data['email']
            phone_number=form.cleaned_data['phone_number']
            username=email.split('@')[0]
            password=form.cleaned_data['password']
            user=Account.objects.create_user(first_name=first_name,last_name=last_name,email=email,password=password,username=username)
            user.phone_number=phone_number
            user.save()
            #create a user profile
            profile=UserProfile()
            profile.user_id=user.id
            profile.profile_picture='default/default-user.png'
            profile.save()
            #email activation
            current_site=get_current_site(request)
            mail_subject="Please activate your account"
            message=render_to_string('accounts/account_verification_email.html',{
                'user':user,
                'domain':current_site,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                'token':default_token_generator.make_token(user),

            })
            to_email=email
            send_mail=EmailMessage(mail_subject,message,to=[to_email])
            send_mail.send()
            messages.success(request,"Registration Successful")
            return redirect('register')
    else:
        form=RegistrationForm()
    context={
        'form':form,
    }
    return render(request,'accounts/register.html',context)

def login(request):
    if request.method=="POST":
        email=request.POST['email']
        password=request.POST['password']
        user=auth.authenticate(email=email,password=password)
        if user is not None:
            auth.login(request,user)
            messages.success(request,"You have been successfully logged in")
            return redirect('home')

    return render(request,'accounts/login.html')

def activate(request,uidb64,token):
    try:
        uid=urlsafe_base64_decode(uidb64).decode()
        user=Account._default_manager.get(pk=uid)
    except(TypeError,ValueError,OverflowError,Account.DoesNotExist):
        user=None
    if user is not None and default_token_generator.check_token(user,token):
        user.is_active=True
        user.save()
        messages.success(request,"Congratulations your account is activated")
        return redirect('login')
    else:
        messages.error(request,"Invalid Activation link")
        return redirect('register')
    

@login_required(login_url="login")
def logout(request):
    auth.logout(request)
    messages.success(request,"You are successfully logout")
    return redirect('login')

def forgotpassword(request):
    if request.method=="POST":
        email=request.POST['email']
        if Account.objects.filter(email=email).exists():
            user=Account.objects.get(email__exact=email)
            current_site=get_current_site(request)
            mail_subject="Reset Your Password"
            message=render_to_string('accounts/reset_password_email.html',{
                'user':user,
                'domain':current_site,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                'token':default_token_generator.make_token(user),

            })
            to_email=email
            send_mail=EmailMessage(mail_subject,message,to=[to_email])
            send_mail.send()
            messages.success(request,"Password reset email has been sent to ur email address")
            return redirect('login')
        else:
            messages.error(request,"Account does not exist")
            return redirect('forgotpassword')
    return render(request,'accounts/forgotpassword.html')


def resetpassword_validate(request,uidb64,token):
    try:
        uid=urlsafe_base64_decode(uidb64).decode()
        user=Account._default_manager.get(pk=uid)
    except(TypeError,ValueError,OverflowError,Account.DoesNotExist):
        user=None
    if user is not None and default_token_generator.check_token(user,token):
        request.session['uid']=uid
        messages.success(request,"please reset your password")
        return redirect('resetpassword')
    else:
        messages.error(request,"This link has been expired")
        return redirect('login')
    

def resetpassword(request):
    if request.method=="POST":
        password=request.POST['password']
        confirm_password=request.POST['confirm_password']
        if password==confirm_password:
            uid=request.session.get('uid')
            user=Account.objects.get(pk=uid)
            user.set_password(password)
            user.save()
            messages.success(request,"Password reset successful")
            return redirect('login')
        else:
            messages.error(request,"password do not match")
            return redirect('resetpassword')
    else:
        return render(request,'accounts/resetpassword.html')


#plumber registration
def plumberregister(request):
    if request.method=='POST':
        form=PlumberProfileFrom(request.POST)
        # print(form)
        if form.is_valid():
            first_name=form.cleaned_data['first_name']
            last_name=form.cleaned_data['last_name']
            email=form.cleaned_data['email']
            phone_number=form.cleaned_data['phone_number']
            username=email.split('@')[0]
            password=form.cleaned_data['password']
            user=PlumberProfile.objects.create_user(first_name=first_name,last_name=last_name,email=email,password=password,username=username)
            user.phone_number=phone_number
            user.save()
            #create a user profile
            profile=PlumberProfile()
            profile.user_id=user.id
            profile.profile_picture='default/default-user.png'
            profile.save()
            #email activation
            current_site=get_current_site(request)
            mail_subject="Please activate your plumber account"
            message=render_to_string('accounts/plumber_verification_email.html',{
                'user':user,
                'domain':current_site,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                'token':default_token_generator.make_token(user),
            })
            to_email=email
            print(to_email)
            send_mail=EmailMessage(mail_subject,message,to=[to_email])
            send_mail.send()
            messages.success(request,"Registration Successful")
            return redirect('plumberregister')
    else:
        form=PlumberProfileFrom()
    context={
        'form':form,
    }
    return render(request,'accounts/plumberregister.html',context)

#plumber login
def plumberlogin(request):
    if request.method=="POST":
        email=request.POST['email']
        print(email)
        password=request.POST['password']
        user=auth.authenticate(email=email,password=password)
        if user is not None:
            auth.login(request,user)
            messages.success(request,"You have been successfully logged in")
            return redirect('home')
        else:
            messages.error(request,'error')
            return redirect('plumberregister')
    return render(request,'accounts/plumberlogin.html')


def plumberactivate(request,uidb64,token):
    try:
        uid=urlsafe_base64_decode(uidb64).decode()
        print(uid)
        user=PlumberProfile._default_manager.get(pk=uid)
        print(user)
    except(TypeError,ValueError,OverflowError,PlumberProfile.DoesNotExist):
        user=None
    if user is not None and default_token_generator.check_token(user,token):
        user.is_active=True
        user.save()
        messages.success(request,"Congratulations your account is activated")
        return redirect('plumberlogin')
    else:
        messages.error(request,"Invalid Activation link")
        return redirect('plumberregister')


# def render_xl(request):
#     response = HttpResponse(content_type='text/csv')
#     temp_list = []
#     writer = csv.writer(response)
#     writer.writerow(['Email'])
#     newsletter=Newsletter.objects.all()
#     for i in newsletter:
#         temp = i.email
#         temp_list.append(temp)
#     writer.writerow(temp_list)
#         # print(i.email)
    
#     response['Content-Disposition'] = 'attachment; filename="Plumberji_emails.csv"'

#     return response