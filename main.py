from flask import Flask, jsonify
from flask_jwt_extended import JWTManager
from app.api.alunos_routes import alunos_bp
from app.api.auth_routes import auth_bp
from config.security import configure_jwt

app = Flask(__name__)

# Configura JWT para proteger todas as rotas
jwt = configure_jwt(app)

# Registra os blueprints da API
app.register_blueprint(alunos_bp)
app.register_blueprint(auth_bp)

@app.after_request
def aplicar_cabecalhos_de_seguranca(response):
    """Adiciona cabeçalhos de segurança em todas as respostas"""
    response.headers["X-Frame-Options"] = "DENY"
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["X-XSS-Protection"] = "1; mode=block"
    response.headers["Strict-Transport-Security"] = "max-age=31536000; includeSubDomains"
    return response

@app.route("/")
def home():
    return jsonify({"home": "There is nothing here for you."})

if __name__ == "__main__":
    app.run(debug=True)