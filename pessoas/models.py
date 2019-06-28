from django.db import models

class Pessoa(models.Model):
    SEXOS = [
        ('m', 'Masculino'), 
        ('f', 'Feminino')
    ]
    
    nome            = models.CharField(max_length=250)
    sexo            = models.CharField(max_length=1, choices=SEXOS)
    data_nascimento = models.DateField()

#-------------------------------------------------------------------------------

class Contato(models.Model):
    pessoa      = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    descricao   = models.CharField(max_length=50)
    telefone    = models.CharField(max_length=50)
    email       = models.CharField(max_length=50)

#-------------------------------------------------------------------------------

class Endereco(models.Model):
    pessoa      = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    descricao   = models.CharField(max_length=50)
    logradouro  = models.CharField(max_length=150)
    numero      = models.CharField(max_length=10)
    complemento = models.CharField(max_length=100)
    bairro      = models.CharField(max_length=100)
    municipio   = models.CharField(max_length=100)
    estado      = models.CharField(max_length=100)