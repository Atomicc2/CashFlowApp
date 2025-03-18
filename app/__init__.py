# main project
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager


# Inicializa as extenções
db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()

def create_app():
    # Cria o app com o nome do arquivo
    app = Flask(__name__)
    
    # Importa as configurações pra inicializar o site da pasta especificada
    app.config.from_pyfile('../config.py')

    # Inicializa as extenções com o app
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'

    # Registra os blueprints
    #from app.routes.auth import auth_bp
    #from app.routes.dashboard import dashboard_bp
    #from app.routes.transactions import transactions_bp

    # Registear os blueprints
    #app.register_blueprint(auth_bp)
    #app.register_blueprint(dashboard_bp)
    #app.register_blueprint(transactions_bp)

    # Importando as tabelas que serão criadas
    from app.models import user
    # Cria as tabelas do banco de dados (caso não existam)
    with app.app_context():
        db.create_all()
 
    return app
    