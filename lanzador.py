from clases.ejercicio1 import *
from clases.ejercicio2 import *

def main1():
        caracteres = ['A', 'F', '1', '3', '0', 'M', 'T']
        frecuencias = [0.2, 0.17, 0.13, 0.21, 0.05, 0.09, 0.15]
        raiz = arboldehuffman(caracteres, frecuencias)
        print("al comprimir cada caracter obtendremos el siguiente codigo: ")
        print("Para la A: ", comprimirtexto('A', raiz))
        print("Para la F: ", comprimirtexto('F', raiz))
        print("Para el 1: ", comprimirtexto('1', raiz))
        print("Para el 3: ", comprimirtexto('3', raiz))
        print("Para el 0: ", comprimirtexto('0', raiz))
        print("Para la M: ", comprimirtexto('T', raiz))
        print("Para la T: ", comprimirtexto('M', raiz))
        print("por ejemplo al codificar la palabra M0T0MAM1 obtenemos el siguiente codigo: ", comprimirtexto('M0T0MAM1', raiz))

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


def main3():
    print("lo siento, no he sido capaz de resolver este ejercicio")


def main():
    n=int(input("¿Que ejercicio deseas hacer?: "))
    if n == 1:
        main1()
    elif n == 2:
        main2()
    elif n == 3:
        main3()
    else:
        print("No has seleccionado ningun ejercicio valido")