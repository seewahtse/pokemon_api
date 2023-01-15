import pokemon_repository as pr
import pokemoncaught
import random

pokemon1 = pokemoncaught.PokemonCaught(12, "rychu", "electric", 67, 98)
pokemon2 = pokemoncaught.PokemonCaught(11, "meowmon", "normal", 63, 128)
pokemon3 = pokemoncaught.PokemonCaught(9, "gengar", "ghost", 234, 23)
repo = pr.PokemonRepository()

pokemons = [pokemon1, pokemon2, pokemon3]

class PokemonService(repo):
    def get_pokemon_by_id(self, id):
        return repo.get_by_id(id)

    def catch_pokemon(self, pokeball):
        if pokeball == "normal":
            probability = random.randint(1, 25)
            if probability == 1:
                print("pokemon caught")
                pc = random.choice(pokemons)
                repo.add_pokemon(pc)
            else:
                print("pokemon got away")
        elif pokeball == "master":
            print("pokemon caught")
            pc = random.choice(pokemons)
            repo.add_pokemon(pc)
        else:
            print("invalid pokeball")









