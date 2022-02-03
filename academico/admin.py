from django.contrib import admin

from academico.models import Pessoa, Endereco, Professor, Aluno, Disciplina, Curso, Matricula

admin.site.register(Pessoa)
admin.site.register(Endereco)
admin.site.register(Professor)
admin.site.register(Aluno)
admin.site.register(Disciplina)
admin.site.register(Curso)
admin.site.register(Matricula)
