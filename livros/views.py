from django.shortcuts import render
from django.http import HttpRequest, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
from .models import Livro
from .models import Autor
from .models import Editora
from .models import Genero

#CRUD Livros#############################################################################

def index(request):

    context = {

        "livros": Livro.objects.all(),
        "titulo_pagina": "Livros"

    }

    return render(request, 'livros/index.html', context)

def cadastro_livro(request):

    context = {

        "autores": Autor.objects.all(),
        "editoras": Editora.objects.all(),
        "generos": Genero.objects.all(),
        "titulo_pagina": "Cadastro de Livro",
        "modo": "Cadastrar"

    }

    request.session["modo"] = "Inserir"

    return render(request, 'livros/cadastro_livro.html', context)

def salvar_livro(request):

    context = {

        "livros": Livro.objects.all(),
        "titulo_pagina": "Livros"

    }

    if(request.method == "GET"):

        livro = Livro(

            titulo = request.GET.get('txt_titulo'),
            data_lancamento = request.GET.get('txt_data'),
            sinopse = request.GET.get('txt_sinopse')

        )

        livro.autor_id = request.GET.get('slt_autor')
        livro.genero_id = request.GET.get('slt_genero')
        livro.editora_id = request.GET.get('slt_editora')

        if(request.session["modo"] == "Atualizar"):

            Livro.objects.filter(id=request.session["id_livro"]).update(

                titulo = livro.titulo,
                data_lancamento = livro.data_lancamento,
                sinopse = livro.sinopse,
                autor_id = livro.autor_id,
                editora_id = livro.editora_id,
                genero_id = livro.genero_id

            )

        else:

            livro.save()

    return render(request, 'livros/index.html', context)

def obter_livro(request, id_livro):

    livro = Livro.objects.filter(id=id_livro)

    context = {

        "livros":livro[0],
        "autores": Autor.objects.all(),
        "editoras": Editora.objects.all(),
        "generos": Genero.objects.all(),
        "titulo_pagina": "Atualização de Livro",
        "modo": "Atualizar"

    }

    livro[0].data_lancamento = livro[0].data_lancamento.strftime("%Y-%m-%d")

    request.session["id_livro"] = id_livro
    request.session["modo"] = "Atualizar"

    return render(request, 'livros/cadastro_livro.html', context)

@csrf_exempt
def visualizar_livro(request):

    if(request.method == "POST"):

        livro = Livro.objects.filter(id=request.POST.get('id_livro'))

        autor = livro[0].autor
        editora = livro[0].editora
        genero = livro[0].genero

        livro = Livro.objects.filter(id=request.POST.get('id_livro')).values()

        livro = list(livro)

        data = livro[0]["data_lancamento"]

        livro[0]["autor"] = autor.nome
        livro[0]["editora"] = editora.nome
        livro[0]["genero"] = genero.nome
        livro[0]["data_lancamento"] = data.strftime("%d/%m/%Y")

        return JsonResponse(livro, safe=False)


def remover_livro(request, id_livro):

    Livro.objects.filter(id=id_livro).delete()

    context = {"livros":Livro.objects.all()}

    return render(request, 'livros/index.html', context)

#CRUD Autores#######################################################################################

def autores(request):

    context = {

        "autores": Autor.objects.all(),
        "titulo_pagina": "Autores"

    }

    return render(request, 'livros/autores.html', context)
