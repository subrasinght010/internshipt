from django.db import models
from django.contrib.auth.models import User

# Create your models here.


# class User(AbstractBaseUser):
#     first_name = models.CharField(max_length=30)
#     last_name = models.CharField(max_length=30)
#     username = models.CharField(max_length=150, unique=True)
#     email = models.EmailField(unique=True)
#     user_type = models.CharField(choices=USER_TYPE_CHOICES, max_length=30)
#     profile_pic = models.ImageField(upload_to='profile_pics/', blank=True, null=True)

#     USERNAME_FIELD = 'username'

#     def __str__(self):
#         return self.username



class Address(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    line1 = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    pincode = models.CharField(max_length=6)
    
    def __str__(self):
        return self.line1


class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.user.username
    

class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.user.username


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    user_type = models.CharField(blank=False, max_length=30)

    
    def __str__(self):
        return self.user.username

