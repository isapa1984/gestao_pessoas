from django.db import models
from pessoas.models import Pessoa

class Divisao(models.Model):
    nome            = models.CharField(max_length = 50)
    ativo           = models.BooleanField()
    data_criacao    = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.nome

# -------------------------------------------------

class Setor(models.Model):
    divisao         = models.ForeignKey(Divisao, on_delete = models.CASCADE)
    nome            = models.CharField(max_length = 50)
    ativo           = models.BooleanField()
    data_criacao    = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.nome

# -------------------------------------------------

class Lotacao(models.Model):
    pessoa          = models.ForeignKey(Pessoa, on_delete = models.CASCADE)
    setor           = models.ForeignKey(Setor, on_delete = models.CASCADE)
    data_criacao    = models.DateTimeField(auto_now_add = True)
    data_inicio     = models.DateField()
    data_termino    = models.DateField()