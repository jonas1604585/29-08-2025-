from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('entrar/', views.entrar, name='entrar'),
    path('sair/', views.sair, name='sair'),

    path('listar/', views.listar, name='listar'),
    path('criar/', views.criar, name='criar'),
    path('editar/<int:id>/', views.editar, name='editar'),
    path('excluir/<int:id>/', views.excluir, name='excluir'),

    path('listarr/<int:id>/', views.listarr, name='listarr'),
    path('criarr/<int:id>/', views.criarr, name='criarr'),
    path('editarr/<int:id>/', views.editarr, name='editarr'),
    path('excluirr/<int:id>/', views.excluirr, name='excluirr'),
]

