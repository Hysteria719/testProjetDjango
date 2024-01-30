from django.shortcuts import render

from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.response import Response

from .models import Categorie
from .models import Article
from .serializers import CategorySerialize
from .serializers import ArticleSerialize

from django.http import JsonResponse
from django.core.serializers import serialize

import json





class CategoryViewset(ReadOnlyModelViewSet):
    serializer_class = CategorySerialize
    def get_queryset(self):
        return Categorie.objects.all()

# filtre uniquement les cat non détruit 
class CategoryNoDestroy(ReadOnlyModelViewSet):
    serializer_class = CategorySerialize
    def get_queryset(self):
        return Categorie.objects.filter(is_destroy=False)   

    

class ArticleViewset(ReadOnlyModelViewSet):
    serializer_class = ArticleSerialize
    def get_queryset(self):
        return Article.objects.all()

# Filtre par id catégorie (http://127.0.0.1:8000/api/art-by-idcat/?category_id=1)    
class ArtSearchByIdCat(ReadOnlyModelViewSet):
    serializer_class = ArticleSerialize
    queryset = Article.objects.all()
    
    
    def get_queryset(self):
        category_id = self.request.GET.get('category_id')
        if category_id is not None:
            queryset = Article.objects.filter(categorie_id=category_id)             
        else : 
            queryset = Article.objects.all()
        return queryset

def devices_json(request):
    #devices = Article.objects.all()

    #json_data = serialize('json', devices, fields=('id', 'titre','contenu','responsable'))
    devices = Article.objects.values('titre', 'contenu', 'responsable__user__username')

   # data_list = json.loads(json_data)
    '''

    for data in data_list:
        #data['fields']['responsible_user'] = data['fields']['responsable'][0]['fields']['user'][0]['fields']['username']
        responsible_user = data['fields']['responsable']
        data['fields']['responsible_user'] = responsible_user
    '''
    data_list = list(devices)
    return JsonResponse(data_list, safe=False)


        


