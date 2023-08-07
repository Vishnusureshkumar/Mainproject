from django.db import models
from django.contrib.auth.models import AbstractBaseUser

# Create your models here.
# class User(AbstractBaseUser):

#     is_admin=models.BooleanField('Is_admin',default=False)
#     is_member=models.BooleanField('Is_member',default=False)
#     is_staff=models.BooleanField('Is_staff',default=False)



class Regcomplaint(models.Model):
    #username=models.ForeignKey()
    name = models.CharField(max_length=15,null=True)
    flatblock=models.CharField(max_length=4,null=True)
    flatno=models.IntegerField(null=True)
    date =models.DateField()
    email=models.EmailField(null=True)
    phoneno=models.IntegerField(null=True)
    complainttitle =models.CharField(max_length=20)
    complaintmedia =models.ImageField(upload_to='images')
    complaintdescription =models.TextField(max_length=500)

class Feedback(models.Model):
    feed_sub=models.CharField(max_length=100) #feedback subject
    feed_description=models.TextField() #feedback description

    def __str__(self):
        return self.feed_sub


