from django.urls import path
from . import views

urlpatterns = [
    path('', views.ContatoListCreate.as_view(), name='contatos-list-create'),
    path('contatos/ordenados/', views.ContatoOrderedList.as_view(), name='contatos-ordered-list'),
    path('contatos/<int:pk>/', views.ContatoRetrieveUpdateDestroy.as_view(), name='contatos-detail'),
]