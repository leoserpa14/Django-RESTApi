from django.db import models

# Create your models here.

class Hero(models.Model):
    name = models.CharField(max_length=60)
    alias = models.CharField(max_length=60)

    def __str__(self):
        # tells Django what to print when it needs to print out an instance of the Hero model
        return self.name



class Friend(models.Model):
    # id = models.PositiveIntegerField(primary_key=True) # Não preciso pq faz automático se eu não boto nada
    name = models.CharField(max_length=60)

class Belonging(models.Model):
    name = models.CharField(max_length=60)

class Borrowed(models.Model):
    what = models.ForeignKey(Belonging, on_delete=models.CASCADE)
    to_who = models.ForeignKey(Friend, on_delete=models.CASCADE)
    when = models.DateTimeField(auto_now_add=True)
    returned = models.DateTimeField(null=True, blank=True)


class OwnedModel(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # daonde que vem esse 'settings'????? Tutorial horrível não fala, e da erro nisso. Ja tentei importar de todo lugar
    class Meta:
        abstract = True
