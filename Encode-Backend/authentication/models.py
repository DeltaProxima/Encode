from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    auth_token = models.CharField(max_length=100,default="")
    isDriver = models.BooleanField(default=False)
    isVerified = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user}'s Profile"