# from django.shortcuts import render
from rest_framework import viewsets
from .models import ToDo
from .serializers import ToDoSerializer


# Create your views here.
class ToDoViewSet(viewsets.ModelViewSet):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer
