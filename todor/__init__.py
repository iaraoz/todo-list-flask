# LAS configuraciones basicas se hacen en este archivo, todo relacionado a la APP

from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    #Configuracion del proyecto
    app.config.from_mapping(
        # Debug fue cambiado a false el 20 de Julio
        DEBUG = False,
        SECRET_KEY = 'devtodo',
        SQLALCHEMY_DATABASE_URI = 'sqlite:///todolist.db'
    )

    db.init_app(app)
    #Registrar Bluprint
    from . import todo, auth
    app.register_blueprint(todo.bp)
    app.register_blueprint(auth.bp)

    @app.route('/')
    def index():
        return render_template("index.html")
    
    with app.app_context():
        db.create_all()

    return app