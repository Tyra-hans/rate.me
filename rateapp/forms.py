from django import forms
from .models import Project,Profile


class UploadProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ['user','pub_date']