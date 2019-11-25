from django.db import models
from vote.models import VoteModel
from django.contrib.auth.models import User



class Project(models.Model):
    author = models.ForeignKey(User, related_name="projects")
    title = models.CharField(max_length=144)
    description = models.CharField(max_length=144)
    project_pic = models.ImageField(upload_to="project_pics/")
    publish_date = models.DateTimeField(auto_now_add=True)

    def save_project(self):
        self.save()



    def __str__(self):
        return self.title

    

    @classmethod
    def get_single_project(cls,id):
        project = cls.objects.get(id=id)
        return project

class Profile(models.Model):
    user = models.OneToOneField(User)
    bio = models.TextField(blank=True)
    prof_pic = models.ImageField(upload_to="prof_pics/")

    def save_profile(self):
        self.save()

    def get_user_projects(self):
        return self.projects.all

    def __str__(self):
        return self.user.username

class Review(models.Model):
    design = models.IntegerField(default=0)
    usability = models.IntegerField(default=0)
    content = models.IntegerField(default=0)
    average = models.IntegerField(default=0)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.project

    


