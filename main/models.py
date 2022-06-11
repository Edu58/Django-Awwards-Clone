from distutils.command.upload import upload
from re import T
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(null=True, blank=True)
    portfolio = models.URLField(null=True, blank=True)
    github = models.URLField(null=True, blank=True)


class Project(models.Model):
    title = models.CharField(max_length=50, null=False, blank=False)
    landing_page = models.ImageField(upload_to='photos/', null=False, blank=False)
    description = models.TextField(null=True, blank=True)
    link = models.URLField(null=True, blank=True)
    user = models.ForeignKey(User, related_name='projects', on_delete=models.CASCADE)