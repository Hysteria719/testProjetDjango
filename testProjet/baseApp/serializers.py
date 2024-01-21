from rest_framework.serializers import ModelSerializer
from .models import Categorie
from .models import Article



class ArticleSerialize(ModelSerializer):        
    class Meta:
        model = Article
        fields = ['id', 'titre', 'contenu', 'categorie', 'date_creation', 'date_modification']

class CategorySerialize(ModelSerializer):
    articles = ArticleSerialize(many=True)
    class Meta:
        model = Categorie
        fields = ['id', 'nom', 'articles'] 
        #ci-dessus 'articles' permet d'afficher les articles dans chaque categorie grace à related_name dans la class Article de models.py