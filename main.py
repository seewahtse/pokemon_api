from flask import Flask, request
from flask_restful import Resource, Api, abort, reqparse, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
db.create_all()

class pokemon_model(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    species = db.Column(db.String(100), nullable=False)
    height = db.Column(db.Integer, nullable=False)
    weight = db.Column(db.Integer, nullable=False)



    # def __repr__(self):
    # #     return f'name = {name}, species = {species}, height = {height}, weight = {weight})'



pokemon_put_args = reqparse.RequestParser()
pokemon_put_args.add_argument("name", type=str, help = "name of the pokemon is required", required=True)
pokemon_put_args.add_argument("species", type=str, help = "type/species of the pokemon is required", required=True)
pokemon_put_args.add_argument("height", type=int, help = "height of the pokemon in cm is required", required=True)
pokemon_put_args.add_argument("weight", type=int, help = "weight of the pokemon in kg is required", required=True)

pokemon_update_args = reqparse.RequestParser()
pokemon_update_args.add_argument("name", type=str, help = "name of the pokemon is required")
pokemon_update_args.add_argument("species", type=str, help = "type/species of the pokemon is required")
pokemon_update_args.add_argument("height", type=int, help = "height of the pokemon in cm is required")
pokemon_update_args.add_argument("weight", type=int, help = "weight of the pokemon in kg is required")

resource_fields = {
    'id' : fields.Integer,
    'name' : fields.String,
    'species' : fields.String,
    'height' : fields.Integer,
    'weight' : fields.Integer
}

# pokemon_dict = {"charmander" : {"pokemon_type": "fire", "height_cm" : 70},
#                 "bulbasaur" : {"pokemon_type": "grass", "height_cm" : 40}}

pokemon_dict = {}

def abort_if_pokemon_doesnt_exist(id):
    if id not in pokemon_dict:
        abort(404, message="Pokemon is not valid...")
#
def abort_if_pokemon_exists(id):
    if id in pokemon_dict:
        abort(409, message="pokemon already exists with that name")


class pokemon(Resource):
    @marshal_with(resource_fields)
    def get(self, id):
        # abort_if_pokemon_doesnt_exist(id)
        # args = pokemon_put_args.parse_args()
        result = pokemon_model.query.filter_by(id = id).first()
        if not result:
            abort(409, message="pokemon not found in database")
        # del pokemon_dict[id]
        # if not result:
        #     abort(404, message="could not find pokemon with that id")
        return result

    #this put method below creates the pokemon in memory, not in database
    # def put(self, pokemon_name):
    #     # abort_if_pokemon_exists(pokemon_name)
    #     args = pokemon_put_args.parse_args()
    #     pokemon_dict[pokemon_name] = args
    #     return pokemon_dict[pokemon_name], 201
    @marshal_with(resource_fields)
    def post(self, id):
        args = pokemon_put_args.parse_args()
        result = pokemon_model.query.filter_by(id = id)
        if result:
            abort(409, message = "Pokemon already in database")
        pokemon = pokemon_model(id = id, name = args['name'], species = args['species'], height = args['height'], weight = args['weight'])
        db.session.add(pokemon)
        db.session.commit()
        return pokemon, 201

    def delete(self, id):
        # abort_if_pokemon_doesnt_exist(id)
        result = pokemon_model.query.filter_by(id=id).first()
        if not result:
            abort(409, message="pokemon not found in database")
        db.session.delete(result)
        db.session.commit()
        return 'deleted...', 204,

    @marshal_with(resource_fields)
    def patch(self, id):
        args = pokemon_update_args.parse_args()
        result = pokemon_model.query.filter_by(id=id).first()
        if not result:
            abort(404, message = "pokemon doesn't exist, cannot update")

        if args['name']:
            result.name = args['name']
        if args['species']:
            result.species = args['species']
        if args['height']:
            result.height = args['height']
        if args['weight']:
            result.weight = args['weight']

        db.session.commit()

        return result





    # def patch(self, id)





api.add_resource(pokemon, "/pokemon/<int:id>")

if __name__ == '__main__':
    app.run(debug=True)






