from django.db import models

# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=1000)
    slug = models.SlugField(max_length=1000,unique=True)

    def __str__(self):
        return self.category_name
    

class Service(models.Model):
    service_name = models.CharField(max_length=1000)
    service_image = models.ImageField(upload_to = "photos/service")
    description = models.TextField(max_length=2000)
    service_price = models.IntegerField()
    slug = models.SlugField(max_length=500)
    service_category = models.ForeignKey(Category,on_delete=models.CASCADE)