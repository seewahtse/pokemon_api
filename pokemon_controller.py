from flask import Flask, request, jsonify
import pokemon_service as ps
from flask_restful import Resource, Api, abort, reqparse, fields, marshal_with

pokemon_service = ps.PokemonService()


class PokemonController:
    def get_pokemon_by_id(self, id):
        return pokemon_service.get_pokemon_by_id(id)

    def catch_pokemon(self, pokeball):
        return pokemon_service.catch_pokemon(pokeball)


app = Flask(__name__)
pokemon_api = PokemonController()


@app.route("/pokemon/<int:id>", methods=["GET"])
def get_pokemon_by_id(id):
    return pokemon_api.get_pokemon_by_id(id)


@app.route("/pokemon/catch/<string:pokeball>", methods=["POST"])
def catch_pokemon(pokeball):
    return pokemon_api.catch_pokemon(pokeball)


if __name__ == '__main__':
    app.run(debug=True)
