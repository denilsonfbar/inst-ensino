from django.db import models
from django.urls import reverse

class Pessoa(models.Model):
    cpf = models.CharField(max_length=14)
    nome = models.CharField(max_length=100)
    data_nascimento = models.DateField()

class Endereco(models.Model):
    pessoa = models.ForeignKey(Pessoa, on_delete=models.RESTRICT)
    logradouro = models.CharField(max_length=100)
    numero = models.CharField(max_length=10)
    bairro = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)
    estado_sigla = models.CharField(max_length=2)
    cep = models.CharField(max_length=11)

class Professor(Pessoa):
    registro_funcional = models.CharField(max_length=10)

class Aluno(Pessoa):

    """ Retorna a URL para acessar os detalhes deste aluno. """
    def get_absolute_url(self):
        return reverse('aluno-detalhes', args=[str(self.id)])


class Disciplina(models.Model):
    professor = models.ForeignKey(Professor, on_delete=models.RESTRICT)
    pre_requisitos = models.ManyToManyField('Disciplina')
    codigo = models.CharField(max_length=10)
    nome = models.CharField(max_length=50)

class Curso(models.Model):
    disciplinas = models.ManyToManyField(Disciplina)
    alunos = models.ManyToManyField(Aluno, through='Matricula')
    codigo = models.CharField(max_length=10)
    nome = models.CharField(max_length=50)

class Matricula(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.RESTRICT)
    curso = models.ForeignKey(Curso, on_delete=models.RESTRICT)
    numero = models.CharField(max_length=15)
