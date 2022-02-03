from django.shortcuts import render
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
