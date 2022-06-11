from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


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


class Rating(models.Model):
    design = models.FloatField(null=False, blank=False, validators=[MinValueValidator(0.0), MaxValueValidator(10.0)])
    usability = models.FloatField(null=False, blank=False, validators=[MinValueValidator(0.0), MaxValueValidator(10.0)])
    content = models.FloatField(null=False, blank=False, validators=[MinValueValidator(0.0), MaxValueValidator(10.0)])
    project = models.ForeignKey(Project, related_name='ratings', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='user_ratings', on_delete=models.CASCADE)