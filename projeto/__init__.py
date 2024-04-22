from flask import Flask
from projeto.lista_filmes import resultado_filmes
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///livros.sqlite3'
db.init_app(app)

from projeto import routes