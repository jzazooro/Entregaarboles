from clases.ejercicio2 import *


def main2():
    data = None
    listadepokemon=[]
    data = leerdataset(data)
    for i in range(len(data)):
        pokemon = pokemon()
        pokemon.id=data['#'].iloc[i]
        pokemon.name=data['Name'].iloc[i]
        pokemon.type1=data['Type 1'].iloc[i]
        pokemon.type2=data['Type 2'].iloc[i]
        pokemon.total=data.Total.iloc[i]
        pokemon.hp=data.HP.iloc[i]
        pokemon.attack=data.Attack.iloc[i]
        pokemon.defense=data. Defense.iloc[i]
        pokemon.sp_atk=data['Sp. Atk'].iloc[i]
        pokemon.sp_def=data['Sp. Def'].iloc[i]
        pokemon.speed=data.Speed.iloc[i]
        pokemon.generation=data.Generation.iloc[i]
        pokemon.legendary=data.Legendary.iloc[i]
        listadepokemon.append(pokemon)

main2()