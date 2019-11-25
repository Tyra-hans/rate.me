from django.shortcuts import render,redirect

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from .models import Profile, Project , Review  
from .forms import UploadProjectForm , UpdateProfileForm ,ReviewForm
# from .serializers import PersonSerializer ,ProjectSerializer


def landing(request):
    return render(request,'all-posts/landing.html')

def home(request):
    context = {
        'projects': Project.objects.all(),
        
    }
    return render(request, 'all-posts/home.html', context)

def profile(request, username):
    user = User.objects.get(username = username)
    profile = Profile.objects.get(user = user)
    projects = Project.objects.filter(author = user)
    return render(request, 'all-posts/profile.html', {'profile': profile, 'projects': projects})

def search(request):
    if 'site' in request.GET and request.GET['site']:
        search_term = request.GET.get('site')
        projects = Project.objects.filter(title__icontains = search_term)
        message = f'{search_term}'
        return render(request, 'all-posts/search.html', {'projects': projects, 'message': message})
        
    return render(request, 'all-posts/search.html')

def project(request, id):
    if request.user.is_authenticated:
        user = User.objects.get(username = request.user)
    project = Project.objects.get(id = id)
    reviews = Review.objects.filter(project = project)
    design = reviews.aggregate(Avg('design'))['design__avg']
    usability = reviews.aggregate(Avg('usability'))['usability__avg']
    content = reviews.aggregate(Avg('content'))['content__avg']
    average = reviews.aggregate(Avg('average'))['average__avg']
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.average = (review.design + review.usability + review.content) / 3
            review.project = project
            review.user = user
            review.save()
        return redirect('project', id)
    else:
        form = ReviewForm()
    return render(request, 'project.html', {'project': project, 'reviews': reviews, 'form': form, 'design': design, 'usability': usability, 'content': content, 'average': average})



@login_required(login_url='/accounts/login/')
def create_post(request):
    if request.method == 'POST':
        form = UploadProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.user = request.user
            project.save()
        return redirect('landing')
    else:
        form = UploadProjectForm()

    return render(request, 'all-posts/create_post.html', {'form': form})


@login_required(login_url='/accounts/login')
def update_profile(request):
    
    my_prof = Profile.objects.get(user=request.user)
    form = UpdateProfileForm(instance=request.user)
    
    
    if request.method == 'POST':
        updateProf = UpdateProfileForm(request.POST,request.FILES,instance=request.user.profile)
        if updateProf.is_valid():
            updateProf.save()
            
            
        return redirect('home')
    else:
        form = UpdateProfileForm(instance=request.user.profile)
    
      
    return render(request, 'all-posts/update_profile.html', {'form': form})