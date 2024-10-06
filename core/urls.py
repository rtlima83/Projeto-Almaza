from django.urls import path
from .views import index, sobre, contato, cardapio 

urlpatterns = [
    path('', index, name='index'),
    path('sobre', sobre, name='sobre'),
    path('cardapio', cardapio, name='cardapio'),
    path('contato', contato, name='contato'),
]
