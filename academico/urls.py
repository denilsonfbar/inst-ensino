from django.urls import path
from academico import views

urlpatterns = [
    path('', views.index, name='index'),
    path('alunos/', views.AlunoListView.as_view(), name='alunos'),
    path('aluno/<int:pk>', views.AlunoDetailView.as_view(), name='aluno-detalhes'),
    path('aluno/create/', views.AlunoCreate.as_view(), name='aluno-create'),
    path('autor/<int:pk>/update/', views.AlunoUpdate.as_view(), name='aluno-update'),
    path('autor/<int:pk>/delete/', views.AlunoDelete.as_view(), name='aluno-delete'),
]
