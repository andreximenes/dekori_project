# -*- coding: utf-8 -*-
from django.shortcuts import render
from core.models import *
from django.http import HttpResponseRedirect


def index(request):
    # galeria = Galeria.objects.get(pk=1)
    try:
        galerias = Galeria.objects.filter(ativo= 1)
        galeria = galerias[0];
    except:
        galeria = None;
    return render(request, 'inicio/index.html', {'galeria': galeria})


def site (request):
    return render (request, 'sobre/sobre.html',)


def sobre (request):
    return render (request, 'sobre/sobre.html',)


def pagina_acessorios (request):
    acessorios = Produto.objects.filter(categoria_id= 4)

    return render (request, 'produtos_lista.html',
            {'produtos': acessorios,
             'titulo': 'Acessórios'}
    )

def menu (request, opcao_menu):

    #Atributos padrão, em caso de algum problema, retornara para a pagina inicial
    produto = None;
    pagina = None;
    titulo = None;


    if opcao_menu == 'toalhas':
        produto = Produto.objects.filter(categoria_id= 1)
        titulo  = 'Toalhas';
        pagina  = 'produtos_lista.html'

    elif opcao_menu == 'suportes':
        produto = Produto.objects.filter(categoria_id= 2)
        titulo  = 'Suportes';
        pagina  = 'produtos_lista.html'

    elif opcao_menu == 'passadeiras':
        produto = Produto.objects.filter(categoria_id= 3)
        titulo  = 'Passadeiras';
        pagina  = 'produtos_lista.html'

    elif opcao_menu == 'acessorios':
        produto = Produto.objects.filter(categoria_id= 4)
        titulo  = 'Acessórios';
        pagina  = 'produtos_lista.html'
    else :
        sobre(request)

    return render (request, pagina,
            {'produtos': produto,
             'titulo': titulo}
    )