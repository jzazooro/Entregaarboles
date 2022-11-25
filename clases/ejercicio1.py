class nodoarbol:

    def __init__(self, simbolo, frecuencia):
        self.izquierda = None
        self.derecha = None
        self.padre = None
        self.simbolo = simbolo
        self.frecuencia = frecuencia

    def buscar(raiz, clave):
        pos=None
        if raiz is not None:
            if raiz.simbolo == clave:
                pos = raiz
                return pos
            if pos == None:
                pos = buscar(raiz.izquierda, clave)
            if pos == None:
                pos = buscar(raiz.derecha, clave)
        return pos
    