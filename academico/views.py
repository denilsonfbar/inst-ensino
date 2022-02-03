from django.shortcuts import render

def index(request):

    # Renderizando o template index.html com os dados da variável contexto:
    return render(request, 'index.html')
