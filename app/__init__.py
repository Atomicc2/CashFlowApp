# main project
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

# Inicializa as extensões
db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()

def create_app():
    # Cria o app com o nome do arquivo
    app = Flask(__name__)
    
    # Importa as configurações pra inicializar o site da pasta especificada
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cashflow.db'
    app.config['SECRET_KEY'] = 'sua_chave_secreta'

    # Inicializa as extensões com o app
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)

    # Importando os modelos das tabelas
    from app.models.user import User
    from app.models.category import Category
    from app.models.transaction import Transaction
    
    login_manager.login_view = 'auth.login'

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))  # Carrega o usuário pelo ID

    # Registra os blueprints
    from app.routes.auth import auth_bp
    from app.routes.index import index_bp
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(index_bp)

    # Cria as tabelas do banco de dados (caso não existam)
    with app.app_context():
        db.create_all()

    return app
