from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def usuarios(request):
    lista_usuarios = [
    {"nome": "Michael Douglas","idade": "23"},
    {"nome": "James Wilson","idade": "55"},
    {"nome": "Peter Parker","idade": "22"},
]
    return render(request, 'usuarios.html', {'usuarios': lista_usuarios})