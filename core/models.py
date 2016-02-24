# -*- coding: utf-8 -*-
from django.db import models

#categoria
class Categoria(models.Model):
    descricao = models.CharField(max_length=100)

    def __unicode__(self):
        return self.descricao

    def subCategorias(self):
        lista = SubCategoria.objects.filter(categoria_pai_id= self.id)
        return lista

#sub-categoria
class SubCategoria(models.Model):
    descricao = models.CharField(max_length=100)
    categoria_pai = models.ForeignKey(Categoria)

    def __unicode__(self):
        return self.descricao


#formato-produto
class FormatoProduto(models.Model):
    descricao = models.CharField(u'Formato do Produto', max_length=100)

    def __unicode__(self):
        return self.descricao


# produto
class Produto (models.Model):
    nome = models.CharField(u'Nome', max_length=120,)
    formato = models.ForeignKey(FormatoProduto, null=True, blank=True)
    categoria = models.ForeignKey(Categoria)
    subcategoria = models.ForeignKey(SubCategoria, null=True, blank=True)
    descricao = models.TextField(
        u'Descrição do Produto',
        max_length=2048,
    )
    thumbnail = models.ImageField(
        u'Imagem Principal',
        null=True,
        blank=True,
        upload_to='produtos',
    )

    ativo = models.BooleanField(default=True)

    def __unicode__(self):
        return self.nome


class AlbumProduto(models.Model):
    produto = models.ForeignKey(Produto)
    img = models.ImageField(
        u'imagem 1',
        upload_to='produtos',
    )


class Galeria(models.Model):
    nome =  models.CharField(
        u'Nome',
        max_length=120,
    )
    img1 = models.ImageField(
        u'imagem 1',
        upload_to='produtos/galeria',
    )
    img2 = models.ImageField(
        u'imagem 2',
        upload_to='produtos/galeria',
    )
    img3 = models.ImageField(
        u'imagem 3',
        upload_to='produtos/galeria',
    )
    img4 = models.ImageField(
        u'imagem 4',
        upload_to='produtos/galeria',
    )

    ativo = models.BooleanField(default=False)

    def __unicode__(self):
        return self.nome