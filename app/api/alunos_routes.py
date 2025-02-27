# Arquivo: alunos_routes.py
from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required  # Adicionamos a proteção
from services.alunos_service import listar_alunos

alunos_bp = Blueprint('alunos', __name__)

def adicionar_links(aluno):
    """Adiciona links HATEOAS a um aluno."""
    return {
        **aluno,
        "links": [
            {
                "rel": "self",
                "href": f"/alunos/{aluno['id']}",
                "method": "GET"
            },
            {
                "rel": "delete",
                "href": f"/alunos/{aluno['id']}",
                "method": "DELETE"
            },
            {
                "rel": "add",
                "href": "/alunos",
                "method": "POST"
            }
        ]
    }

@alunos_bp.route('/alunos', methods=['GET'])
@jwt_required()  # Agora exige autenticação
def buscar_alunos():
    alunos = listar_alunos()

    alunos_com_links = [adicionar_links(aluno) for aluno in alunos]

    response = jsonify(alunos_com_links)
    response.headers['Cache-Control'] = 'public, max-age=300'

    return response

@alunos_bp.route('/alunos/<int:aluno_id>', methods=['GET'])
@jwt_required()  # Agora exige autenticação
def obter_aluno(aluno_id):
    alunos = listar_alunos()
    aluno = next((a for a in alunos if a["id"] == aluno_id), None)

    if not aluno:
        return jsonify({"erro": "Aluno não encontrado"}), 404

    aluno_com_links = adicionar_links(aluno)

    response = jsonify(aluno_com_links)
    response.headers['Cache-Control'] = 'public, max-age=300'

    return response