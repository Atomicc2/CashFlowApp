# main project
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Inicializa as extenções
db = SQLAlchemy()
migrate = Migrate()

def create_app():
    # Cria o app com o nome do arquivo
    app = Flask(__name__)
    
    # Importa as configurações pra inicializar o site da pasta especificada
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cashflow.db'

    # Inicializa as extenções com o app
    db.init_app(app)
    migrate.init_app(app, db)

    # Importando o modelos das tabelas
    from app.models.user import User
    from app.models.category import Category
    from app.models.trasnsaction import Transaction
    
    # Cria as tabelas do banco de dados (caso não existam)
    with app.app_context():
        db.create_all()
 
    return app