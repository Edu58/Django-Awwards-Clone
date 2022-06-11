from django.test import TestCase
from django.contrib.auth.models import User
from .models import Profile, Project, Rating


# Create your tests here.
# class TestProfile(TestCase):
#     def setUp(self):
#         self.john = User(username="john", first_name="john", last_name="bravo", email="john@gmail.com", password="john98765")

#     def tearDown(self):
#         self.john.delete()

#     def test_user_instance(self):
#         self.john.save()
#         self.assertTrue(isinstance(self.john, User))

#     def test_profile_instance(self):
#         self.john.save()
#         self.john_profile = Profile(user=self.john ,bio="I am johny bravo", portfolio="https://johnthedev.com", github="https://github.com/john")
#         self.john_profile.save()

#         self.assertTrue(isinstance(self.john_profile, Profile))
        
#     def test_profile_creation(self):
#         self.john.save()
#         self.john_profile = Profile(user=self.john ,bio="I am johny bravo", portfolio="https://johnthedev.com", github="https://github.com/john")
#         self.john_profile.save()

#         self.assertTrue(self.john.profile.bio, "I am johny bravo")
#         self.assertTrue(self.john.profile.portfolio, "https://johnthedev.com")
#         self.assertTrue(self.john.profile.github, "https://github.com/john")


# class TestProject(TestCase):
#     def setUp(self):
#         self.john = User(username="john", first_name="john", last_name="bravo", email="john@gmail.com", password="john98765")
#         self.john.save()

#         self.new_project = Project(
#             title="Awaards Clone",
#             landing_page="./static/images/default-website-landing-page.png",
#             description="This is a clone for the famous Awaards website",
#             link="https://awaards-clone.co.ke",
#             user=self.john
#         )

#         self.new_project_with_no_landing_page = Project(
#             title="Awaards Clone",
#             description="This is a clone for the famous Awaards website",
#             link="https://awaards-clone.co.ke",
#             user=self.john
#         )

#     def tearDown(self):
#         self.john.delete()

#     def test_project_instance(self):
#         self.new_project.save()
#         self.assertTrue(self.new_project, Project)

#     def test_missing_landing_page(self):
#         self.new_project_with_no_landing_page.save()
#         self.assertTrue(self.new_project, Project)
#         self.assertTrue(self.new_project_with_no_landing_page.landing_page,
#                         './static/images/default-website-landing-page.png')


class TestRating(TestCase):
    def setUp(self):
        self.john = User(username="john", first_name="john",
                         last_name="bravo", email="john@gmail.com", password="john98765")
        self.john.save()

        self.new_project = Project(
            title="Awaards Clone",
            landing_page="./static/images/default-website-landing-page.png",
            description="This is a clone for the famous Awaards website",
            link="https://awaards-clone.co.ke",
            user=self.john
        )

        self.new_project.save()

        self.new_rating = Rating(
            design=5.0, usability=8.0, content=5.4, project=self.new_project, user=self.john)


    def tearDown(self):
        self.john.delete()

    def test_rating_instance(self):
        self.new_rating.save()
        self.assertTrue(isinstance(self.new_rating, Rating))
    
    def test_rating_data_type(self):
        self.new_rating = Rating(
            design=5, usability=8, content=5.4, project=self.new_project, user=self.john)
        self.new_rating.save()
        self.assertRaises(TypeError)
