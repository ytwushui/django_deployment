from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfileInfo(models.Model):
    # add additional calss the User doesn't have
    # exenting the class, use the one to one filed to
    user = models.OneToOneField(User, on_delete='CASCADE')
    # add additional classes
    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to = 'profile_pic', blank = True)
    # need a pic file
    def __str__(self):
        return self.user.username
