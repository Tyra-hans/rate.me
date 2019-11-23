from django.shortcuts import render,redirect

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
# from .models import Person,Profile, Project , Rating 
# from .serializers import PersonSerializer ,ProjectSerializer, RatingSerializer


def Home(request):
    return render(request,'all-posts/home.html')