from random import choices
from django import forms
from .models import Account, UserProfile,PlumberProfile
class RegistrationForm(forms.ModelForm):

    first_name=forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'Enter Name',
    }))
    password=forms.CharField(widget=forms.PasswordInput(attrs={
        'class':'form-control',
        'placeholder':'Enter Password',
    }))
    confirm_password=forms.CharField(widget=forms.PasswordInput(attrs={
        'class':'form-control',
        'placeholder':'Confirm Password',
    }))
    
    class Meta:
        model=Account
        fields=['first_name','last_name','email','phone_number','password']

    def __init__(self,*args,**kwargs):
        super(RegistrationForm,self).__init__(*args,**kwargs)
        self.fields['first_name'].widget.attrs['placeholder']='Enter First Name'
        self.fields['last_name'].widget.attrs['placeholder']='Enter Last Name'
        self.fields['email'].widget.attrs['placeholder']='Enter Email Address'
        self.fields['phone_number'].widget.attrs['placeholder']='Enter Phone Number'
        

        for field in self.fields:
            self.fields[field].widget.attrs['class']='form-control'

    def clean(self):
        cleaned_data=super(RegistrationForm,self).clean()
        password=cleaned_data.get('password')
        confirm_password=cleaned_data.get('confirm_password')
        #strong password
        if password != confirm_password:
            raise forms.ValidationError(
                "Password doesn't match"
            )
        special_characters = "[~\!@#\$%\^&\*\(\)_\+{}\":;'\[\]]"
        if not any(char.isdigit() for char in password):
            raise forms.ValidationError(
                'Password should contain one digit'
            )
        if not any(char in special_characters for char in password):
            raise forms.ValidationError(
                'Password should contain one special character'
            )
        if len(password) <=5:
            raise forms.ValidationError(
                "This password is too short. It must contain at least 5"
            )
        if not any(char.isalpha() for char in password):
          raise forms.ValidationError(
                "Password must contain at least 1 letter."
            )
class UserForm(forms.ModelForm):
    class Meta:
        model=Account
        fields=['first_name','last_name','phone_number']

class UserProfileForm(forms.ModelForm):
    class Meta:
        model=UserProfile
        fields=['address_line_1','address_line_2','city','state','country','profile_picture']






class PlumberProfileFrom(forms.ModelForm):
    first_name=forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'Enter first_name',
    }))
    last_name=forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'Enter last_name',
    }))
    email=forms.EmailField(widget=forms.EmailInput(attrs={
        'class':'form-control',
        'placeholder':'Enter Email',
    })) 
    phone_number=forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'Enter phone_no',
    }))           
    password=forms.CharField(widget=forms.PasswordInput(attrs={
        'class':'form-control',
        'placeholder':'Enter Password',
    }))
    confirm_password=forms.CharField(widget=forms.PasswordInput(attrs={
        'class':'form-control',
        'placeholder':'Confirm Password',
    }))
    class Meta:
        model=PlumberProfile
        fields=['first_name','last_name','phone_number','email','password']

    def clean(self):
        cleaned_data=super(PlumberProfileFrom,self).clean()
        password=cleaned_data.get('password')
        confirm_password=cleaned_data.get('confirm_password')
        if password != confirm_password:
            raise forms.ValidationError(
                "Password doesn't match"
            )

        #strong password
        special_characters = "[~\!@#\$%\^&\*\(\)_\+{}\":;'\[\]]"
        if not any(char.isdigit() for char in password):
            raise forms.ValidationError(
                'Password should contain one digit'
            )
        if not any(char in special_characters for char in password):
            raise forms.ValidationError(
                'Password should contain one special character'
            )
        if len(password) <=5:
            raise forms.ValidationError(
                "This password is too short. It must contain at least 5"
            )
        if not any(char.isalpha() for char in password):
          raise forms.ValidationError(
                "Password must contain at least 1 letter."
            )
