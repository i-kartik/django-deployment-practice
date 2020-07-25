from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfileInfo(models.Model):
    on_delete=models.DO_NOTHING

    user= models.OneToOneField(User,on_delete)

    #addtional
    portfolio_site=models.URLField(blank=True)
    profile_pic=models.ImageField(upload_to='profile_pics',blank=True)

    def __str__(self):
        return self.user.username
         #username is default attribute of User package
