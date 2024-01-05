import os
import sys
import msvcrt

def convertir_a_matriz(mapa):
    return [list(fila) for fila in mapa.split("\n")]

def limpiar_y_mostrar(matriz):
    os.system('cls' if os.name == 'nt' else 'clear')
    for fila in matriz:
        print("".join(fila))

def main_loop(mapa, pos_inicial, pos_final):
    px, py = pos_inicial

    while (px, py) != pos_final:
        mapa[px][py] = 'P'
        limpiar_y_mostrar(mapa)
        mapa[px][py] = '.'

        key = msvcrt.getch().decode('utf-8')
        nueva_px, nueva_py = px, py

        if key == 'w' and px > 0 and mapa[px - 1][py] != '#':
            nueva_px -= 1
        elif key == 's' and px < len(mapa) - 1 and mapa[px + 1][py] != '#':
            nueva_px += 1
        elif key == 'a' and py > 0 and mapa[px][py - 1] != '#':
            nueva_py -= 1
        elif key == 'd' and py < len(mapa[0]) - 1 and mapa[px][py + 1] != '#':
            nueva_py += 1

        px, py = nueva_px, nueva_py

if __name__ == "__main__":
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

    matriz_laberinto = convertir_a_matriz(laberinto)
    pos_inicial = (0, 0)
    pos_final = (len(matriz_laberinto) - 1, len(matriz_laberinto[0]) - 1)

    main_loop(matriz_laberinto, pos_inicial, pos_final)
