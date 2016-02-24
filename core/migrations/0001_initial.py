# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AlbumProduto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('img', models.ImageField(upload_to=b'produtos', verbose_name='imagem 1')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descricao', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='FormatoProduto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descricao', models.CharField(max_length=100, verbose_name='Formato do Produto')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Galeria',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=120, verbose_name='Nome')),
                ('img1', models.ImageField(upload_to=b'produtos/galeria', verbose_name='imagem 1')),
                ('img2', models.ImageField(upload_to=b'produtos/galeria', verbose_name='imagem 2')),
                ('img3', models.ImageField(upload_to=b'produtos/galeria', verbose_name='imagem 3')),
                ('img4', models.ImageField(upload_to=b'produtos/galeria', verbose_name='imagem 4')),
                ('ativo', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=120, verbose_name='Nome')),
                ('descricao', models.TextField(max_length=2048, verbose_name='Descri\xe7\xe3o do Produto')),
                ('thumbnail', models.ImageField(upload_to=b'produtos', null=True, verbose_name='Imagem Principal', blank=True)),
                ('ativo', models.BooleanField(default=True)),
                ('categoria', models.ForeignKey(to='core.Categoria')),
                ('formato', models.ForeignKey(blank=True, to='core.FormatoProduto', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SubCategoria',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descricao', models.CharField(max_length=100)),
                ('categoria_pai', models.ForeignKey(to='core.Categoria')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='produto',
            name='subcategoria',
            field=models.ForeignKey(blank=True, to='core.SubCategoria', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='albumproduto',
            name='produto',
            field=models.ForeignKey(to='core.Produto'),
            preserve_default=True,
        ),
    ]
