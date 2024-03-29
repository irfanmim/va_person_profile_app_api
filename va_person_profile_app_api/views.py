from django.shortcuts import render
from rest_framework import viewsets
from .models import Profile
from .serializers import ProfileSerializer
from rest_framework.parsers import MultiPartParser

# Create your views here.
class ProfileView(viewsets.ModelViewSet):
    #/profile
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
