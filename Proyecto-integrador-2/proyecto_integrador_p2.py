from readchar import readkey, key

print("Presiona la tecla ↑ para salir.")

while True:
    tecla = readkey() # Lee un caracter del teclado

    if tecla == key.UP:
        break

    print(f"Tecla presionada: {tecla}") # Imprime una tecla y realiza una acción

print("¡Gracias por jugar!")
