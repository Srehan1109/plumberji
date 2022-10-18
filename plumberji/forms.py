from django.forms import ModelForm
from .models import Enquiry
from django import forms

class EnquiryForm(forms.ModelForm):
    job_to_be_done=forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'Your Plumbing Tasks:',
        'border':'1 px solid black',
    }))

    first_name=forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'Enter first_name',
    }))
    last_name=forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'Enter first_name',
    }))
    contact_number=forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'Enter Your Phone Number',
    }))
    email=forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'Enter Your Email ',
    }))
    city=forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'Enter Your City Name ',
    }))

    class Meta:
        model = Enquiry
        fields = ['job_to_be_done','first_name','last_name','contact_number','email','city']