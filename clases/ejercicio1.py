class nodoarbol:

    def __init__(self, simbolo, frecuencia):
        self.izquierda = None
        self.derecha = None
        self.padre = None
        self.simbolo = simbolo
        self.frecuencia = frecuencia

def buscar(raiz, clave):
    posicion = None
    if raiz is not None:
        if raiz.simbolo == clave:
            posicion = raiz
            return posicion
        if posicion == None:
            posicion = buscar(raiz.izquierda, clave)
        if posicion == None:
            posicion = buscar(raiz.derecha, clave)
    return
    