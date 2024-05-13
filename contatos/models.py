from django.db import models



class Contatos(models.Model):
   nome = models.CharField(max_length=60)
   email = models.EmailField()
   telefone = models.CharField(max_length=25)
   endereco = models.CharField(max_length=70)

   def __str__(self):
       
    return self.nome


