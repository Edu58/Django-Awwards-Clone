from django.test import TestCase
from django.contrib.auth.models import User
from .models import Profile, Project, Rating


# Create your tests here.
class TestProfile(TestCase):
    def setUp(self):
        self.john = User(username="john", first_name="john", last_name="bravo", email="john@gmail.com", password="john98765")

    def test_user_instance(self):
        self.john.save()
        self.assertTrue(isinstance(self.john, User))
        
    def test_profile_creation(self):
        self.john.save()
        self.john_profile = Profile(user=self.john ,bio="I am johny bravo", portfolio="https://johnthedev.com", github="https://github.com/john")
        self.john_profile.save()

        self.assertTrue(self.john.profile.bio, "I am johny bravo")
        self.assertTrue(self.john.profile.portfolio, "https://johnthedev.com")
        self.assertTrue(self.john.profile.github, "https://github.com/john")
