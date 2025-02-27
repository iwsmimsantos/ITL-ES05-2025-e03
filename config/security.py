from flask_jwt_extended import JWTManager

def configure_jwt(app):
    app.config["JWT_SECRET_KEY"] = "sua_chave_secreta"  # Defina uma chave secreta real
    jwt = JWTManager(app)
    return jwt