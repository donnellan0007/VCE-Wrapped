from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    suburb = models.CharField(max_length=100, blank=True, null=True) # city, suburb, town etc
    zip_code = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(upload_to='profile_image', blank=True)
    def __str__(self):
        return self.name