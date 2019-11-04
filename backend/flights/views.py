from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from rest_framework import viewsets
from .serializers import UserSerializer


def index(request):
    return HttpResponse("<h1>Hello, Flight Scheduler!</h1>")


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
