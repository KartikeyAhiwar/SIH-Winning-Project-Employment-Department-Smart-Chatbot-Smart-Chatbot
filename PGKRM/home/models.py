from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    phone=models.CharField(max_length=10)
    address=models.TextField()
    dob=models.DateTimeField(null=False)
    state=models.CharField(max_length=30)
    gender=models.CharField(max_length=12,default='Male')
    city=models.CharField(max_length=30)
    profession=models.CharField(max_length=30)
    skill=models.CharField(max_length=100)
    photo = models.ImageField(upload_to='photos')

CustomUser._meta.get_field("groups").remote_field.related_name = "customuser_groups"
CustomUser._meta.get_field("user_permissions").remote_field.related_name = "customuser_user_permissions"