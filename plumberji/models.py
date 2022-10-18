from django.db import models

# Create your models here.


class Enquiry(models.Model):
    job_to_be_done = models.CharField(
    max_length=50, blank=True, null=True)
    first_name = models.CharField(max_length=155)
    last_name = models.CharField(max_length=155)
    contact_number = models.IntegerField()
    email=models.EmailField(max_length=100,null=True,blank=True,unique=True )
    city = models.CharField(max_length=155)

    def __str__(self):
        return self.first_name + " " + self.last_name
    def __str___(self):
        return self.email
    class Meta():
        verbose_name_plural = 'Enquiries'
