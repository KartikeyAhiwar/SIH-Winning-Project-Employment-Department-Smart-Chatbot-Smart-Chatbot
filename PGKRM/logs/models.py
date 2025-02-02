from django.db import models
from home.models import CustomUser

class Log(models.Model):
    profile = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=True, null=True)
    photo = models.ImageField(upload_to='logs')
    is_correct = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)