from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pokemoncaught

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
db.create_all()


class PokemonRepository:

    def get_by_id(self, id):
        return db.query.filter_by(id = id).first()

    def add_pokemon(self, pc):
        db.session.add(pc)
        db.session.commit()
        return 201