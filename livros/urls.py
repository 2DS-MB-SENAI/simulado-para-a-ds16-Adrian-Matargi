from django.urls import path
from .views import listar_livros, livros_api

urlpatterns = [
    path('', listar_livros, name='listar_livros'),
    path('api/livros/', livros_api, name='livros_api'),
]