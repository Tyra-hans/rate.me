from django.test import TestCase
from .models import Project, Profile , Review

class ProjectTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.project1= Project(title = 'Titl1', description = 'Lorem Ipsum' )

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.project1,Project))

 

    # Testing String representation Method
    def test_string_representation(self):
        project = Project(title="sometext")
        self.assertEqual(str(project), 'sometext')

class ProfileTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.prof= Profile(bio = 'Titl1', prof_pic = 'profpic.png' )

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.prof,Profile))

 

    # Testing String representation Method
    def test_string_representation(self):
        profile = Profile(bio="sometext")
        self.assertEqual(str(profile), 'sometext')

class ReviewTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.rev= Review(bio = 'Titl1', prof_pic = 'profpic.png' )

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.prof,Profile))

 

    # Testing String representation Method
    def test_string_representation(self):
        profile = Profile(bio="sometext")
        self.assertEqual(str(profile), 'sometext')

