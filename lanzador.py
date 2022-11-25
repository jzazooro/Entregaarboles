from clases.ejercicio1 import *

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

def main():
    main1()
main()