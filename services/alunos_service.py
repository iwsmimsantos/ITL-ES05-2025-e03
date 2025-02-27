# Arquivo: alunos_service.py

from repositories.alunos_repository import obter_todos_alunos

def listar_alunos():
    return obter_todos_alunos()