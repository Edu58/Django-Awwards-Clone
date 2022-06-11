from re import T
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(null=True, blank=True)
    portfolio = models.URLField(null=True, blank=True)
    github = models.URLField(null=True, blank=True)