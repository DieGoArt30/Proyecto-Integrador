"""from readchar import readkey, key

print ("Presiona una tecla. Para salir, presiona la tecla de flecha hacia arriba (UP).")

while True:
    # Lee un caracter del teclado
    tecla = readkey()

    # Verifica si la tecla es la flecha hacia arriba (UP)
    if tecla == key.UP:
        break

    # Imprime la tecla presionada
    print(f"Tecla presionada:", tecla)

print("Programa finalizado.")
"""
from readchar import readkey, key

print("Presiona la tecla ↑ para salir.")

while True:
    tecla = readkey() # Lee un caracter del teclado

    if tecla == key.UP:
        break

    print(f"Tecla presionada: {tecla}") # Imprime una tecla y realiza una acción

print("¡Gracias por jugar!")