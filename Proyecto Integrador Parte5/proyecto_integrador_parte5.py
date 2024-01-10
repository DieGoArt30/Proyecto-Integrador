import os
import random
from readchar import readkey, key

class Juego:
    def __init__(self, mapa, posicion_inicial, posicion_final):
        self.mapa = self.convertir_mapa_a_matriz(mapa)
        self.posicion_inicial = posicion_inicial
        self.posicion_final = posicion_final

    def convertir_mapa_a_matriz(self, laberinto):
        return [list(fila) for fila in laberinto.split("\n")]

    def limpiar_pantalla(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def mostrar_mapa(self):
        self.limpiar_pantalla()
        for fila in self.mapa:
            print("".join(fila))

    def verificar_posicion_valida(self, px, py):
        return 0 <= px < len(self.mapa[0]) and 0 <= py < len(self.mapa) and self.mapa[py][px] != "#"

    def actualizar_posicion(self, tecla, px, py):
        movimientos = {
            key.UP: (0, -1),
            key.DOWN: (0, 1),
            key.LEFT: (-1, 0),
            key.RIGHT: (1, 0)
        }

        movimiento = movimientos.get(tecla, (0, 0))
        nueva_px, nueva_py = px + movimiento[0], py + movimiento[1]

        return (nueva_px, nueva_py) if self.verificar_posicion_valida(nueva_px, nueva_py) else (px, py)

    def main_loop(self):
        px, py = self.posicion_inicial

        while (px, py) != self.posicion_final:
            self.mapa[py][px] = "P"
            self.mostrar_mapa()

            tecla = readkey()

            self.mapa[py][px] = "."

            px, py = self.actualizar_posicion(tecla, px, py)

        print("¡Has logrado salir del Laberinto, nos vemos en el siguiente módulo!")

class JuegoArchivo(Juego):
    def __init__(self, path_a_mapas):
        mapa, posicion_inicial, posicion_final = self.leer_mapa_aleatorio(path_a_mapas)
        super().__init__(mapa, posicion_inicial, posicion_final)

    def leer_mapa_aleatorio(self, path_a_mapas):
        archivos = os.listdir(path_a_mapas)

        if archivos:
            nombre_archivo = random.choice(archivos)
            path_completo = os.path.join(path_a_mapas, nombre_archivo)

            with open(path_completo, 'r') as archivo:
                contenido = archivo.read()
                return self.procesar_contenido_mapa(contenido)

    def procesar_contenido_mapa(self, contenido):
        lineas = contenido.strip().split("\n")
        mapa = "\n".join(lineas[1:])  # Ignorar la primera línea que contiene las dimensiones
        coordenadas_inicio = tuple(map(int, lineas[0].split()))
        posicion_inicial = coordenadas_inicio[:2]
        posicion_final = coordenadas_inicio[2:]
        return mapa, posicion_inicial, posicion_final

if __name__ == "__main__":
    # Puedes cambiar la ruta a la carpeta de mapas
    path_a_mapas = r"C:\Users\DIEGO ARTEAGA\Documents\ADA SCHOOL\mapas"

    # Usar la nueva clase JuegoArchivo
    juego_archivo = JuegoArchivo(path_a_mapas)
    juego_archivo.main_loop()
