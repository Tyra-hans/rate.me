from django import forms
from .models import Project,Profile, Review


class UploadProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ['user','pub_date']

class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        exclude = ['average','project', 'user']