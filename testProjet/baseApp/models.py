from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    is_admin = models.BooleanField(default=False)
    is_system = models.BooleanField(default=False)

class DevTeams(models.Model):
    nom = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete = models.CASCADE, null=True)

    

class Categorie(models.Model):
    nom = models.CharField(max_length=255, unique=True)
    is_destroy = models.BooleanField(default=False)

    def __str__ (self):
        return self.nom
#related_name attribut inverse permettant de renvoyer les valeurs d'article dans categorie 
class Article(models.Model):
    titre = models.CharField(max_length=255)
    contenu = models.TextField()
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE, related_name='articles')
  #  auteur = models.ForeignKey(User, on_delete = models.CASCADE)
    date_creation = models.DateTimeField(auto_now_add=True)
    date_modification = models.DateTimeField(auto_now=True)

    

    



