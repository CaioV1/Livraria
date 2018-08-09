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
    

]
