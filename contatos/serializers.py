from rest_framework import serializers
from .models import Contatos


class ContatoSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Contatos
        fields = '__all__'
        
        
"""
    Este código cria um serializer no Django REST Framework para o modelo 
    Contatos`, garantindo que todos os campos do modelo sejam incluídos na serialização. 
    O serializer converte objetos do modelo em formato de dados (por exemplo, JSON) e vice-versa, 
    facilitando a manipulação de dados do modelo através de uma API RESTful.
 """        