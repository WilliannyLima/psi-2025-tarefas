from django.shortcuts import render
from datetime import date
from .models import Tarefa

def index(request):
    hoje = date.today()
    tarefas = Tarefa.objects.all()
    return render(request, 'tarefas/index.html', {'tarefas': tarefas, 'hoje': hoje})

