from django.db import models
from django.shortcuts import reverse
from django import forms


# Create your models here.
from django.db import models

class Orders(models.Model):
    topic = models.CharField(max_length=255, blank=True, null=True )
    pages = models.IntegerField(default=0,  blank=True, null=True)
    style = models.CharField(max_length=255,  blank=True, null=True)
    subject = models.CharField(max_length=500,  blank=True, null=True)
    amount = models.IntegerField(default=0.0, blank=True, null=True)
    instructions = models.TextField(max_length=5000,  blank=True, null=True)
    uploads = models.FileField( upload_to="Upload_files/%Y%m%d/" , max_length=255,  blank=True, null=True,)
    created_at = models.DateTimeField(auto_now_add=True,  blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True,  blank=True, null=True)

    def get_absolute_url(self):
        return reverse('Home:index')
        
class UploadFiles(models.Model):
    files = models.FileField(upload_to = "Upload_files/%Y%m%d/" , max_length=255,  blank=True, null=True )
    main = models.BooleanField(default=False)
    

class VueOrders(models.Model):
    Type = models.CharField(max_length = 200, blank=True, null=True  )
    pages = models.CharField(max_length = 200, blank=True, null=True  )
    service =  models.CharField(max_length = 200, blank=True, null=True  )
    Level =  models.CharField(max_length = 200, blank=True, null=True  )
    deadline = models.DateTimeField( blank=True, null=True)
    fin_earl = models.BooleanField(default=False )
    language = models.CharField(default=200,max_length=200, blank=True, null= True)
    Topic = models.CharField( max_length= 500, blank=True, null=True )
    sources = models.IntegerField(default=0)
    style = models.CharField( max_length=200 ,blank=True, null=True )
    subject = models.CharField( max_length= 500, blank=True, null=True)
    instructions = models.TextField(max_length=5000,  blank=True, null=True)
    files = models.ManyToManyField(UploadFiles)
    complete = models.BooleanField(default=False)













