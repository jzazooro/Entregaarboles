# Entregaarboles

El enlace al repositorio de GitHub de este proyecto es el siguiente: [GitHub](https://github.com/jzazooro/Entregaarboles.git)

He resuelto tres ejercicios propuestos sobre arboles, nodos, grafos...

El codigo usado es el siguiente:

### ejercicio1:

```
class nodoarbol:

    def __init__(self, caracter, frecuencia):
        
        self.izquierda = None
        self.derecha = None
        self.padre = None
        self.caracter = caracter
        self.frecuencia = frecuencia

def buscar(raiz, clave):
    
    posicion = None
    
    if raiz is not None:
        if raiz.caracter == clave:
            posicion = raiz
            return posicion
        if posicion == None:
            posicion = buscar(raiz.izquierda, clave)
        if posicion == None:
            posicion = buscar(raiz.derecha, clave)
    return posicion

def ordenarobjetos(lista):
    
    lista = sorted(lista, key=lambda x: x.caracter)
    lista = sorted(lista, key=lambda x: x.frecuencia)
    return lista

def meternodoalarbol(lista, nodo):
    
    for i in range(len(lista)):
        if lista[i].frecuencia > nodo.frecuencia:
            lista.insert(i, nodo)
            break
        if i == len(lista)-1:
            lista.append(nodo)
            break
    return lista

def arboldehuffman(caracteres, frecuencias):
    
    nodos = []
    
    for i in range(len(caracteres)):
        nodos.append(nodoarbol(caracteres[i], frecuencias[i]))
    nodos = ordenarobjetos(nodos)
    
    while len(nodos)>1:
        nodo = nodoarbol('XX', nodos[0].frecuencia + nodos[1].frecuencia)
        nodo.izquierda = nodos[0]
        nodo.izquierda.padre = nodo
        nodo.derecha = nodos[1]
        nodo.derecha.padre = nodo
        nodos = meternodoalarbol(nodos, nodo)
        nodos.pop(1)
        nodos.pop(0)
    return nodos[0]

def comprimirtexto(mensaje, raiz):
    
    codigo=[]
    
    mensaje = mensaje[::-1]
    for m in mensaje:
        nodo = buscar(raiz, m)
        while nodo.padre is not None:
            if nodo.padre.izquierda == nodo:
                codigo.append('0')
            else: 
                codigo.append('1')
            nodo = nodo.padre

    codigo = codigo[::-1]
    return ''.join(codigo)

def descomprimirtexto(codigo, raiz):
    
    mensaje = []
    nodo = raiz
    
    for c in codigo:
        if nodo.derecha is None:
            mensaje.append(nodo.caracter)
            nodo = raiz
        if c == '0':
            nodo = nodo.izquierda
        else:
            nodo = nodo.derecha
    
    mensaje.append(nodo.caracter)
    return ''.join(mensaje)
```

### ejercicio 2:

```

```

### ejercicio 3:

```

```

### lanzador:

```

```

### main:

```
from lanzador import main

if __name__ == '__main__':
    main()
```
