from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
import uuid
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
    name = models.CharField(max_length=200,blank=True,null=True)
    last_name = models.CharField(max_length=200,blank=True,null=True)
    username = models.CharField(max_length=200,blank=True,null=True)
    email = models.EmailField(max_length=500, blank=True,null=True)
    short_intro = models.CharField(max_length=200,blank=True,null=True)
    bio  = models.TextField(blank=True,null=True)
    profile_image = models.ImageField(null=True,blank=True ,upload_to='profiles/',default='profiles/default_profile.png' )
    social_github = models.CharField(max_length=200,blank=True,null=True)
    social_twitter = models.CharField(max_length=200,blank=True,null=True)
    social_linkedin = models.CharField(max_length=200,blank=True,null=True)
    social_youtube = models.CharField(max_length=200,blank=True,null=True)
    social_website = models.CharField(max_length=200,blank=True,null=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)
    
    def __str__(self):
        return str(self.username)




class skill(models.Model):
    owner = models.ForeignKey(Profile,on_delete=models.CASCADE,null=True,blank=True)
    name = models.CharField(max_length=200 , blank=True, null=True)
    description = models.TextField(null=True,blank=True)

    def __str__(self):
        return str(self.name)

class todo(models.Model):
    owner = models.ForeignKey(Profile,on_delete=models.CASCADE,null=True,blank=True)
    name = models.CharField(max_length=200 , blank=True, null=True)
    description = models.TextField(null=True,blank=True)

    def __str__(self):
        return str(self.name)



