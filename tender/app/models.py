from django.db import models
from tinymce.models import HTMLField
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Category(models.Model):
    category_name = models.CharField( max_length=50)
    category_desc = models.CharField( max_length=500)

    def __str__(self):
        return self.category_name
    
class Region(models.Model):
    region= models.CharField(max_length=50)
    desc = models.CharField( max_length=500)
    def __str__(self):
        return self.region
    
class Tender(models.Model):
    title = models.CharField( max_length=1000)
    bidClosingDate = models.DateTimeField( auto_now=False, auto_now_add=False)
    bidOpeningDate = models.DateTimeField(auto_now=False, auto_now_add=False)
    publishedOn = models.CharField( max_length=50)
    postedDate = models.DateTimeField(auto_now=False, auto_now_add=True)
    bidDocumentPrice = models.IntegerField(null=True)
    bidBond = models.FloatField(null=True)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    description = HTMLField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    isFree = models.BooleanField()
    postedBy=models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
class Company(models.Model):
    name=models.CharField(max_length=100)
    desc = models.TextField()
    website = models.CharField(null=True, max_length=50)
    email = models.EmailField(null=True, max_length=254)
    phone = PhoneNumberField(blank=True)

    def __str__(self):
        return self.name
    
class DocumentBid(models.Model):
    title = models.CharField( max_length=50)
    desc = models.TextField()
    tender = models.ForeignKey(Tender, on_delete=models.CASCADE)
    price = models.IntegerField()

    def __str__(self):
        return self.title
    
    
    
