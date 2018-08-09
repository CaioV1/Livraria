from django.db import models

class Livro(models.Model):

    titulo = models.CharField(max_length=70)
    autor = models.ForeignKey("Autor", on_delete=models.CASCADE, related_name="autor_livro")
    genero = models.ForeignKey("Genero", on_delete=models.CASCADE, related_name="genero_livro")
    editora = models.ForeignKey("Editora", on_delete=models.CASCADE, related_name="editora_livro")
    data_lancamento = models.DateField()
    sinopse = models.TextField()

class Autor(models.Model):

    nome = models.CharField(max_length=100)
    data_nascimento = models.DateField()
    pais_origem = models.CharField(max_length=100)

class Editora(models.Model):

    nome = models.CharField(max_length=100)

class Genero(models.Model):

    nome = models.CharField(max_length=100)
