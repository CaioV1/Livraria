from django.shortcuts import render
from django.http import HttpRequest, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
from .models import Livro
from .models import Autor
from .models import Editora
from .models import Genero
import json
import os

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

def cadastro_autor(request):

    caminho = os.path.dirname(__file__)
    caminho += "\\static\\livros\\"
    caminhoJSON = os.path.join(caminho, "paises.json")

    #print(caminho)

    with open(caminhoJSON, encoding="utf-8") as file:

        dados = json.load(file)

    context = {

        "titulo_pagina": "Cadastro de Autor",
        "modo": "Cadastrar",
        "paises": dados

    }

    request.session["modo"] = "Inserir"

    return render(request, "livros/cadastro_autor.html", context)

def salvar_autor(request):

    print(request.session["modo"])

    if(request.session["modo"] == "Atualizar"):

        Autor.objects.filter(id=request.session["id_autor"]).update(

            nome = request.GET.get("txt_nome"),
            data_nascimento = request.GET.get("txt_data"),
            pais_origem = request.GET.get("slt_paises")

        )

    else:

        Autor(

            nome = request.GET.get("txt_nome"),
            data_nascimento = request.GET.get("txt_data"),
            pais_origem = request.GET.get("slt_paises")

        ).save()

    context = {"autores":Autor.objects.all()}

    return render(request, "livros/autores.html", context)

def remover_autor(request, id_autor):

    Autor.objects.filter(id=id_autor).delete()

    context = {"autores":Autor.objects.all()}

    return render(request, "livros/autores.html", context)

def obter_autor(request, id_autor):

    autor = Autor.objects.filter(id=id_autor)

    caminho = os.path.dirname(__file__)
    caminho += "\\static\\livros\\"
    caminhoJSON = os.path.join(caminho, "paises.json")

    #print(caminho)

    with open(caminhoJSON, encoding="utf-8") as file:

        dados = json.load(file)

    context = {

        "autor": autor[0],
        "titulo_pagina": "Atualização de Autor",
        "modo": "Atualizar",
        "paises": dados

    }

    request.session["modo"] = "Atualizar"
    request.session["id_autor"] = id_autor

    print(context["autor"])

    return render(request, "livros/cadastro_autor.html", context)

#CRUD Editoras #####################################################################################

def editoras(request):

    context = {

        "editoras": Editora.objects.all(),
        "titulo_pagina": "Editoras"

    }

    return render(request, "livros/editoras.html", context)

def cadastro_editora(request):

    context = {

        "titulo_pagina": "Cadastro de Editora",
        "modo": "Cadastrar"

    }

    request.session["modo"] = "Inserir"

    return render(request, "livros/cadastro_editora.html", context)

def salvar_editora(request):

    if(request.session["modo"] == "Atualizar"):

        Editora.objects.filter(id=request.session["id_editora"]).update(

            nome = request.GET.get("txt_nome")

        )

    else:

        Editora(nome = request.GET.get("txt_nome")).save()

    context = {

        "editoras": Editora.objects.all(),
        "titulo_pagina": "Editoras"

    }

    return render(request, "livros/editoras.html", context)

def remover_editora(request, id_editora):

    Editora.objects.filter(id=id_editora).delete()

    context = {

        "editoras": Editora.objects.all(),
        "titulo_pagina": "Editoras"

    }

    return render(request, "livros/editoras.html", context)

def obter_editora(request, id_editora):

    editora = Editora.objects.filter(id=id_editora)

    context = {

        "editora": editora[0],
        "titulo_pagina": "Atualização de Editora",
        "modo": "Atualizar"

    }

    request.session["modo"] = "Atualizar"
    request.session["id_editora"] = id_editora

    return render(request, "livros/cadastro_editora.html", context)

#CRUD Gêneros #####################################################################################

def generos(request):

    context = {

        "generos": Genero.objects.all(),
        "titulo_pagina": "Gêneros"

    }

    return render(request, "livros/generos.html", context)

def cadastro_genero(request):

    context = {

        "titulo_pagina": "Cadastro de Gênero",
        "modo": "Cadastrar"

    }

    request.session["modo"] = "Inserir"

    return render(request, "livros/cadastro_genero.html", context)

def salvar_genero(request):

    if(request.session["modo"] == "Atualizar"):

        Genero.objects.filter(id=request.session["id_genero"]).update(

            nome = request.GET.get("txt_nome")

        )

    else:

        Genero(nome = request.GET.get("txt_nome")).save()

    context = {

        "generos": Genero.objects.all(),
        "titulo_pagina": "Gêneros"

    }

    return render(request, "livros/generos.html", context)

def remover_genero(request, id_genero):

    Genero.objects.filter(id=id_genero).delete()

    context = {

        "generos": Genero.objects.all(),
        "titulo_pagina": "Gêneros"

    }

    return render(request, "livros/generos.html", context)

def obter_genero(request, id_genero):

    genero = Genero.objects.filter(id=id_genero)

    context = {

        "genero": genero[0],
        "titulo_pagina": "Atualização de Gênero",
        "modo": "Atualizar"

    }

    request.session["modo"] = "Atualizar"
    request.session["id_genero"] = id_genero

    return render(request, "livros/cadastro_genero.html", context)
