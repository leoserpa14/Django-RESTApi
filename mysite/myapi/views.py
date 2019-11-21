from django.shortcuts import render

from rest_framework import viewsets

from .serializers import HeroSerializer, FriendSerializer, BelongingSerializer, BorrowedSerializer
from .models import Hero, Friend, Belonging, Borrowed

# Create your views here.


class HeroViewSet(viewsets.ModelViewSet):
    queryset = Hero.objects.all().order_by('name')
    serializer_class = HeroSerializer



class FriendViewSet(viewsets.ModelViewSet):
    queryset = Friend.objects.all()
    serializer_class = FriendSerializer

class BelongingViewSet(viewsets.ModelViewSet):
    queryset = Belonging.objects.all()
    serializer_class = BelongingSerializer

class BorrowedViewSet(viewsets.ModelViewSet):
    queryset = Borrowed.objects.all()
    serializer_class = BorrowedSerializer