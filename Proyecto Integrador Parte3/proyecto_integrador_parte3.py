import os
import msvcrt  # Solo necesario en Windows para detectar la tecla presionada

def borrar_y_mostrar_numero(numero):
    os.system('cls' if os.name == 'nt' else 'clear')  # Borrar la terminal
    print(f"Número actual: {numero}")

def main():
    numero = 0

    while numero <= 50:
        borrar_y_mostrar_numero(numero)

        # Leer la tecla 'n' del teclado
        tecla = msvcrt.getch().decode('utf-8')  # Solo necesario en Windows

        if tecla.lower() == 'n':
            numero += 1

if __name__ == "__main__":
    main()