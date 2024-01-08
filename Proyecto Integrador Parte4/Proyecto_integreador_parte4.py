import os
from readchar import readkey, key

def convertir_mapa_a_matriz(laberinto):
    # Dividir el laberinto en filas
    filas = laberinto.split("\n")
    matriz = [list(fila) for fila in filas]
    return matriz

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_mapa(mapa):
    limpiar_pantalla()
    for fila in mapa:
        print("".join(fila))

def verificar_posicion_valida(px, py, mapa):
    return 0 <= px < len(mapa[0]) and 0 <= py < len(mapa) and mapa[py][px] != "#"

def actualizar_posicion(tecla, px, py, mapa):
    movimientos = {
        key.UP: (0, -1),
        key.DOWN: (0, 1),
        key.LEFT: (-1, 0),
        key.RIGHT: (1, 0)
    }

    movimiento = movimientos.get(tecla, (0, 0))
    nueva_px, nueva_py = px + movimiento[0], py + movimiento[1]

    if verificar_posicion_valida(nueva_px, nueva_py, mapa):
        return nueva_px, nueva_py
    else:
        return px, py

def main_loop(mapa, posicion_inicial, posicion_final):
    px, py = posicion_inicial

    while (px, py) != posicion_final:
        mapa[py][px] = "P"
        mostrar_mapa(mapa)

        # Leer la tecla presionada
        tecla = readkey()

        # Restaurar la posición anterior antes de verificar si la nueva posición es válida
        mapa[py][px] = "."

        # Actualizar la posición tentativa
        px, py = actualizar_posicion(tecla, px, py, mapa)

    print("¡Has logrado salir del Laberinto, nos vemos en el siguiente módulo!")

laberinto = """..###################
....#...............#
#.#.#####.#########.#
#.#...........#.#.#.#
#.#####.#.###.#.#.#.#
#...#.#.#.#.....#...#
#.#.#.#######.#.#####
#.#...#.....#.#...#.#
#####.#####.#.#.###.#
#.#.#.#.......#...#.#
#.#.#.#######.#####.#
#...#...#...#.#.#...#
###.#.#####.#.#.###.#
#.#...#.......#.....#
#.#.#.###.#.#.###.#.#
#...#.#...#.#.....#.#
###.#######.###.###.#
#.#.#.#.#.#...#.#...#
#.#.#.#.#.#.#.#.#.#.#
#.....#.....#.#.#.#.#
###################.."""

mapa = convertir_mapa_a_matriz(laberinto)
posicion_inicial = (0, 0)
posicion_final = (len(mapa[0]) - 1, len(mapa) - 1)

main_loop(mapa, posicion_inicial, posicion_final)

