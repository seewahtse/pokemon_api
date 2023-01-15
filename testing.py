import random

if __name__ == '__main__':
    pokeball = random.randint(1, 25)
    print(pokeball)
    if pokeball == 1:
        print("pokemon caught")
    else:
        print("pokemon got away")





