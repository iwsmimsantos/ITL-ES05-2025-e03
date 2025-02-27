# Arquivo: auth_routes.py
from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token

auth_bp = Blueprint("auth", __name__)

# Simulação de banco de usuários (em produção, usar um banco real)
usuarios = {"admin": "1234"}

@auth_bp.route("/login", methods=["POST"])
def login():
    """Autenticação para obter um token JWT"""
    dados = request.json
    usuario = dados.get("usuario")
    senha = dados.get("senha")

    if usuario in usuarios and usuarios[usuario] == senha:
        token = create_access_token(identity=usuario)
        return jsonify({"token": token})

    return jsonify({"erro": "Credenciais inválidas"}), 401