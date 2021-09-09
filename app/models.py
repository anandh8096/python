from django.db import models
from django.contrib.auth.models import User


class UserProfileInfo(models.Model):
  user = models.OneToOneField(User)
  portfolio = models.URLField(blank=True)
  profile_pic = models.ImageField(upload_to='profile_pic',blank=True)
  

  def __str__(self):
    return self.user.username

# Create your models here.
#class Topic(models.Model):
 #   top_name = models.CharField(max_length=264,unique=True)

 #   def __str__(self):
  #      return self.top_name




#class Webpage(models.Model):
    #name = models.CharField(max_length=264,unique=True) 
    #url = models.URLField(unique=True) 


    #def __str__(self):
     #    return self.name     
    

#class Users(models.Model):
 #   first_nam = models.CharField(max_length=264)
  #  las_nam = models.CharField(max_length=264)
   # email = models.EmailField(max_length=264,unique=True)

