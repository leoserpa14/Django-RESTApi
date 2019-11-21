# serializers.py

from rest_framework import serializers
from .models import Hero, Friend, Belonging, Borrowed


class HeroSerializer(serializers.HyperlinkedModelSerializer):
    class Meta: # links the Hero with its serializer
        model = Hero
        fields = ('name', 'alias')
        

class FriendSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Friend
        fields = ('id', 'name')

class BelongingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Belonging
        fields = ('id', 'name')

class BorrowedSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Borrowed
        fields = ('id', 'what', 'to_who', 'when', 'returned')
        # lembrar sempre de botar o 'id' em todos aqui no serializers
    