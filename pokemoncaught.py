from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pokemoncaught

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
db.create_all()

class PokemonCaught(db.model):
        id = db.Column(db.Integer, primary_key=True, nullable=False)
        name = db.Column(db.String(100), nullable=False)
        species = db.Column(db.String(100), nullable=False)
        height = db.Column(db.Integer, nullable=False)
        weight = db.Column(db.Integer, nullable=False)


