# -*- coding: utf-8 -*-
from django.shortcuts import render
from core.models import *
from django.http import HttpResponseRedirect


def index(request):
    # galeria = Galeria.objects.get(pk=1)

    galerias = Galeria.objects.filter(ativo= 1)
    galeria = galerias[0];
    return render(request, 'inicio/index_welcome.html',
                  {'galeria': galeria}
    )

def site (request):
    return render (request, 'sobre.html',)


def sobre (request):
    return render (request, 'sobre.html',)



def pagina_toalhas (request):
    toalhas = Produto.objects.filter(categoria_id= 1)

    return render (request, 'produtos_lista.html',
            {'produtos': toalhas,
             'titulo': 'Toalhas'}
    )

def pagina_passadeiras (request):
    passadeiras = Produto.objects.filter(categoria_id= 3)

    return render (request, 'produtos_lista.html',
            {'produtos': passadeiras,
             'titulo': 'Passadeiras'}
    )

def pagina_suportes (request):
    passadeiras = Produto.objects.filter(categoria_id= 2)

    return render (request, 'produtos_lista.html',
            {'produtos': passadeiras,
             'titulo': 'Suportes'}
    )

def pagina_acessorios (request):
    acessorios = Produto.objects.filter(categoria_id= 4)

    return render (request, 'produtos_lista.html',
            {'produtos': acessorios,
             'titulo': 'Acessórios'}
    )