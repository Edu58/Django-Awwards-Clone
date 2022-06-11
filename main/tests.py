from django.test import TestCase
from django.contrib.auth.models import User
from .models import Profile, Project, Rating


# Create your tests here.
class TestProfile(TestCase):
    def setUp(self):
        self.john = User(username="john", first_name="john", last_name="bravo", email="john@gmail.com", password="john98765")
        self.john.save()

    def test_user_instance(self):
        self.assertTrue(isinstance(self.john, User))
        
