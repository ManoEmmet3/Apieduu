
from rest_framework import generics
from .models import Contatos
from .serializers import ContatoSerializer


class ContatoListCreate(generics.ListCreateAPIView):
    queryset = Contatos.objects.all()
    serializer_class = ContatoSerializer
    
class ContatoRetrieveUpdateDestroy(generics.RetrieveUpdateAPIView):
   queryset = Contatos.objects.all()
   serializer_class = ContatoSerializer    
   
class ContatoOrderedList(generics.ListAPIView):
    serializer_class = ContatoSerializer

    def get_queryset(self):
        order_by = self.request.query_params.get('order_by', 'nome')
        return Contatos.objects.order_by(order_by)   
    
