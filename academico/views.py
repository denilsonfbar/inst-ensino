from django.shortcuts import render
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import PermissionRequiredMixin
from academico.models import Pessoa, Endereco, Professor, Aluno, Disciplina, Curso, Matricula

def index(request):

# Contando o número de livros e exemplares:
    num_pessoas = Pessoa.objects.all().count()
    num_professores = Professor.objects.all().count()
    num_alunos = Aluno.objects.all().count()
    num_disciplinas = Disciplina.objects.all().count()
    num_cursos = Curso.objects.all().count()
    num_matriculas = Matricula.objects.all().count()

    contexto = {
        'num_pessoas': num_pessoas,
        'num_professores': num_professores,
        'num_alunos': num_alunos,
        'num_disciplinas': num_disciplinas,
        'num_cursos': num_cursos,
        'num_matriculas': num_matriculas
    }

    # Renderizando o template index.html com os dados da variável contexto:
    return render(request, 'index.html', context=contexto)

class AlunoListView(generic.ListView):

    model = Aluno

class AlunoDetailView(generic.DetailView):

    model = Aluno

class AlunoCreateView(PermissionRequiredMixin, CreateView):
    
    permission_required = 'academico.pode_manipular_aluno'
    model = Aluno
    fields = '__all__'

class AlunoUpdateView(PermissionRequiredMixin, UpdateView):

    permission_required = 'academico.pode_manipular_aluno'
    model = Aluno
    fields = ['nome', 'cpf', 'data_nascimento']

class AlunoDeleteView(PermissionRequiredMixin, DeleteView):

    permission_required = 'academico.pode_manipular_aluno'
    model = Aluno
