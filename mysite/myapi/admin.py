from django.contrib import admin
from .models import Hero, Friend, Belonging, Borrowed
# Register your models here.

# example: I need to tell that I created the 'Hero' model in models.py

admin.site.register(Hero)
admin.site.register(Friend)
admin.site.register(Belonging)
admin.site.register(Borrowed)
