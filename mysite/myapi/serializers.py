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


"""
Se eu quisesse criar meu próprio Serializer:


class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    username = serializers.CharField(max_length=200)
    password = serializers.CharField(max_length=100, style={"input_type":"password"})
    is_staff = serializers.BooleanField(default=False)

    def create(self, validated_data):
        # The function called when you create a new User object/instance

        return User.objects.create(**validated_data)
    
    def update(self, instance, validated_data):

        # Update and return an existing `User` instance, given the validated data.
        
        instance.username = validated_data.get('username', instance.username)
        instance.password = validated_data.get('password', instance.password)
        instance.is_staff = validated_data.get('is_staff', instance.is_staff)
        instance.save()
        return instance


from django.contrib.admin.models import User
from tickets.serializers import UserSerializer
user = User.objects.create(username="oyetoketoby80", password="oyetoketoby80")

userserializer = UserSerializer(user)
userserializer.data
# {'id': 1, 'username': u'oyetoketoby80', 'password':'passwordhash'}
"""
