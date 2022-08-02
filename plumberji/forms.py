from django.forms import ModelForm
from .models import Enquiry


class EnquiryForm(ModelForm):

    class Meta:
        model = Enquiry
        fields = ['job_to_be_done','first_name','last_name','contact_number','email','city']
