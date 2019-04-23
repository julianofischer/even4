from django.db import models

# Create your models here.
# models: Evento, Trabalho, Autor, Área Temática
class Evento(models.Model):
    #titulo
    #local
    #data de publicação
    #apresentação
    #corpo editorial (comissão científica e comissão organizadora)
    #areas temáticas
    #contato
    #edições anteriores
    pass

class Anais(models.Model):
    #titulo
    #ISBN
    #data de publicação
    #país de publicação
    #idioma de publicação
    pass

class Trabalho(models.Model):
    #titulo
    #autores
    #modalidade (artigo, banner, ...)
    #área temática
    #página do trabalho (URL)
    #anais
    #pdf
    pass

class Autor(models.Model):
    #nome
    #nome como citação
    #contato (e-mail)
    #afiliação  (universidade)
    pass

class Afiliacao(models.Model):
    #nome
    #sigla
    #cidade
    #estado
    #país
    pass

class AreaTematica(models.Model):
    pass
