import pygame, sys

class Arbol:  # Clase para representar cada miembro del árbol
    def __init__(self, elemento):
        self.hijos = []         # Lista de hijos del nodo
        self.elemento = elemento  # Nombre del miembro

def agregarElemento(arbol, elemento, elementoPadre):  # Agrega un nuevo nodo al árbol
    subarbol = buscarSubarbol(arbol, elementoPadre)
    if subarbol:
        subarbol.hijos.append(Arbol(elemento))

def buscarSubarbol(arbol, elemento):  # Busca un nodo por nombre
    if arbol.elemento == elemento:
        return arbol
    for subarbol in arbol.hijos:
        arbolBuscado = buscarSubarbol(subarbol, elemento)
        if arbolBuscado:
            return arbolBuscado
    return None

def eliminarElemento(arbol, nombre):  # Elimina un nodo por nombre
    if arbol is None:
        return False
    for i, hijo in enumerate(arbol.hijos):
        if hijo.elemento == nombre:
            del arbol.hijos[i]       # Elimina el hijo de la lista
            return True
        else:
            eliminado = eliminarElemento(hijo, nombre)
            if eliminado:
                return True
    return False

abuela = "Inocenta"
hija1, hija2, hija3 = "Deliao", "Santos", "Vicenta"
nieta2, nieta3 = "Norma", "Rocio"
nieto4, nieto5, nieto6 = "Rosario", "Julio", "Manuel"
hijo1_deliao, hijo2_deliao = "Hijo1Deliao", "Hijo2Deliao"

arbol = Arbol(abuela)
agregarElemento(arbol, hija2, abuela)
agregarElemento(arbol, hija3, abuela)
agregarElemento(arbol, nieto4, hija2)
agregarElemento(arbol, hija1, abuela)
agregarElemento(arbol, nieta2, hija1)
agregarElemento(arbol, nieta3, hija1)
agregarElemento(arbol, nieto6, hija1)

# 👶 Nuevos hijos de Deliao
agregarElemento(arbol, hijo1_deliao, hija1)
agregarElemento(arbol, hijo2_deliao, hija1)

# ❌ Eliminar un miembro antes de mostrar
eliminarElemento(arbol, "Norma")


pygame.init()
ANCHO, ALTO = 800, 600
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Árbol Genealógico de Inocenta Arce")
fuente = pygame.font.SysFont(None, 24)

BLANCO, NEGRO, AZUL = (255, 255, 255), (0, 0, 0), (100, 149, 237)
ESPACIO_X, ESPACIO_Y, RADIO = 120, 100, 30
posiciones = {}

def calcular_posiciones(nodo, x, y):  # Calcula posición de cada nodo
    posiciones[nodo.elemento] = (x, y)
    total_hijos = len(nodo.hijos)
    if total_hijos == 0:
        return
    ancho_total = ESPACIO_X * (total_hijos - 1)
    inicio_x = x - ancho_total // 2
    for i, hijo in enumerate(nodo.hijos):
        calcular_posiciones(hijo, inicio_x + i * ESPACIO_X, y + ESPACIO_Y)

def dibujar_arbol(nodo):  # Dibuja el árbol en pantalla
    x, y = posiciones[nodo.elemento]
    pygame.draw.circle(pantalla, AZUL, (x, y), RADIO)
    texto = fuente.render(nodo.elemento, True, NEGRO)
    pantalla.blit(texto, (x - texto.get_width() // 2, y - texto.get_height() // 2))
    for hijo in nodo.hijos:
        x_h, y_h = posiciones[hijo.elemento]
        pygame.draw.line(pantalla, NEGRO, (x, y), (x_h, y_h), 2)
        dibujar_arbol(hijo)

calcular_posiciones(arbol, ANCHO // 2, 50)

corriendo = True
while corriendo:
    pantalla.fill(BLANCO)
    dibujar_arbol(arbol)
    pygame.display.flip()
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False

pygame.quit()
sys.exit()
