import sys
import juego

def main():
    while True:  # Ciclo principal del juego
        try:
            print("La torre busca personas valientes para completar todos sus pisos...")
            print("[1] Apuntarme a la expedición")
            print("[2] Salir")
            opcion = int(input("Elige una opción: "))
            if opcion == 1:
                juego.juego()  # Llamamos a juego.py 
            elif opcion == 2:
                print("Cerrando juego")
                sys.exit()  # Sale del juego
            else:
                print("Ingresa una opción correcta")
        except ValueError:
            print("Por favor, ingresa una opción válida.")

# Llamada inicial
main()