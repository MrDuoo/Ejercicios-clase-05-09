# Árbol binario para árbol genealógico familiar
# Cada nodo tiene como máximo dos hijos

class Nodo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.izquierda = None
        self.derecha = None

def buscar(nodo, nombre):
    if nodo is None:
        return False
    if nodo.nombre == nombre:
        return True
    return buscar(nodo.izquierda, nombre) or buscar(nodo.derecha, nombre)

def profundidad(nodo):
    if nodo is None:
        return 0
    return 1 + max(profundidad(nodo.izquierda), profundidad(nodo.derecha))

def imprimirArbolBinario(nodo, nivel=0):
    if nodo is not None:
        print("  " * nivel + nodo.nombre)
        imprimirArbolBinario(nodo.izquierda, nivel + 1)
        imprimirArbolBinario(nodo.derecha, nivel + 1)

def eliminar(nodo, nombre):  # Función para eliminar un nodo con cierto nombre
    if nodo is None:         # Si el nodo actual no existe, no hay nada que hacer
        return None          # Retorna None para indicar que no hay nodo

    if nodo.nombre == nombre:  # Si el nombre del nodo actual coincide con el que queremos eliminar
        if nodo.izquierda is None and nodo.derecha is None:  # Caso 1: sin hijos
            return None        # Eliminamos el nodo retornando None

        if nodo.izquierda is None:  # Caso 2a: solo tiene hijo derecho
            return nodo.derecha     # Reemplazamos el nodo por su hijo derecho

        if nodo.derecha is None:    # Caso 2b: solo tiene hijo izquierdo
            return nodo.izquierda   # Reemplazamos el nodo por su hijo izquierdo

        # Caso 3: tiene dos hijos
        sucesor = nodo.derecha      # Buscamos el sucesor en el subárbol derecho
        while sucesor.izquierda:    # El sucesor es el nodo más a la izquierda del subárbol derecho
            sucesor = sucesor.izquierda

        nodo.nombre = sucesor.nombre  # Copiamos el nombre del sucesor al nodo actual
        nodo.derecha = eliminar(nodo.derecha, sucesor.nombre)  # Eliminamos el sucesor duplicado
        return nodo  # Retornamos el nodo actualizado

    # Si no es el nodo a eliminar, seguimos buscando en los hijos
    nodo.izquierda = eliminar(nodo.izquierda, nombre)  # Aplicamos recursivamente a la izquierda
    nodo.derecha = eliminar(nodo.derecha, nombre)      # Aplicamos recursivamente a la derecha
    return nodo  # Retornamos el nodo actual (sin cambios si no fue eliminado)


# Datos de prueba
raiz = Nodo("Abuelos")
raiz.izquierda = Nodo("Padre")
raiz.derecha = Nodo("Tíos")
raiz.izquierda.izquierda = Nodo("Yo")
raiz.izquierda.derecha = Nodo("Hermana")

# Pruebas
print("¿Existe 'Yo'? →", buscar(raiz, "Yo"))  # True
print("Profundidad del árbol →", profundidad(raiz))  # 3

print("\nÁrbol original:")
imprimirArbolBinario(raiz)

# Eliminar un miembro
raiz = eliminar(raiz, "Hermana")

print("\nÁrbol después de eliminar 'Hermana':")
imprimirArbolBinario(raiz)
