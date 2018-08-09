from django.contrib import admin
from django.conf.urls import url, include
from livros import views

urlpatterns = [
    url(r'^$', include('livros.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^livros/', include('livros.urls')),
    #url(r'^livros/autores/', views.autores, name='autores'),
]
