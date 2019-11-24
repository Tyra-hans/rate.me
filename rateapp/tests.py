from django.test import TestCase
from .models import Project, Profile

class ProjectTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.project1= Project(title = 'Titl1', description = 'Lorem Ipsum' )

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.project1,Project))

       # Testing Save Method
    def test_save_method(self):
        self.save_project()
        projects = Project.objects.all()
        self.assertTrue(len(projects) > 0)

        # Testing String representation Method
    def test_string_representation(self):
        project = Project(title="sometext")
        self.assertEqual(str(project), 'sometext')
