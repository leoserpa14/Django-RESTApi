from django.shortcuts import render

from rest_framework import viewsets
from rest_framework import permissions

from .serializers import HeroSerializer, FriendSerializer, BelongingSerializer, BorrowedSerializer
from .models import Hero, Friend, Belonging, Borrowed

# Create your views here.


class HeroViewSet(viewsets.ModelViewSet):
    queryset = Hero.objects.all().order_by('name')
    serializer_class = HeroSerializer


# Posso definir permissões diferentes para cada view, como por exemplo

class FriendViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.DjangoModelPermissions]
    queryset = Friend.objects.all()
    serializer_class = FriendSerializer

class BelongingViewSet(viewsets.ModelViewSet):
    queryset = Belonging.objects.all()
    serializer_class = BelongingSerializer

class BorrowedViewSet(viewsets.ModelViewSet):
    queryset = Borrowed.objects.all()
    serializer_class = BorrowedSerializer