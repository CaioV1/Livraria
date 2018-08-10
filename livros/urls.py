from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^cadastro_livro/', views.cadastro_livro, name='cadastro_livro'),
    url(r'^salvar_livro/', views.salvar_livro, name='salvar_livro'),
    url(r'^visualizar_livro/', views.visualizar_livro, name='visualizar_livro'),
    url(r'^remover_livro/(?P<id_livro>\d+)/$', views.remover_livro, name='remover_livro'),
    url(r'^obter_livro/(?P<id_livro>\d+)/$', views.obter_livro, name='obter_livro'),

    url(r'^autores/', views.autores, name='autores'),
    url(r'^cadastro_autor/', views.cadastro_autor, name='cadastro_autor'),
    url(r"^salvar_autor/", views.salvar_autor, name="salvar_autor"),
    url(r"^remover_autor/(?P<id_autor>\d+)/$", views.remover_autor, name="remover_autor"),
    url(r"^obter_autor/(?P<id_autor>\d+)/$", views.obter_autor, name="obter_autor"),

    url(r"^editoras/", views.editoras, name="editoras"),
    url(r"^cadastro_editora/", views.cadastro_editora, name="cadastro_editora"),
    url(r"^salvar_editora/", views.salvar_editora, name="salvar_editora"),
    url(r"^remover_editora/(?P<id_editora>\d+)/$", views.remover_editora, name="remover_editora"),
    url(r"^obter_editora/(?P<id_editora>\d+)/$", views.obter_editora, name="obter_editora"),

    url(r"^generos/", views.generos, name="generos"),
    url(r"^cadastro_genero/", views.cadastro_genero, name="cadastro_genero"),
    url(r"^salvar_genero/", views.salvar_genero, name="salvar_genero"),
    url(r"^remover_genero/(?P<id_genero>\d+)/$", views.remover_genero, name="remover_genero"),
    url(r"^obter_genero/(?P<id_genero>\d+)/$", views.obter_genero, name="obter_genero")
]
