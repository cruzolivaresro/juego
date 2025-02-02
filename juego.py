import sys

def juego(key):
    while key:  # Solo entra en este ciclo si key es False
        try:
            print("***** Menú *****")
            print("[1] Escoge a tu equipo")
            print("[2] Observa a tu equipo")
            print("[3] Volver al menú anterior")
            opcion = int(input("Elige una opción: "))
            if opcion == 1:
                print("Elige a 3")
                sys.exit()  # Se cierra el juego si elige esta opción
            elif opcion == 2:
                print("Este es tu equipo")
                sys.exit()  # También se cierra si elige esta opción
            elif opcion == 3:
                print("Volviendo al menú principal...")
                return True  # Devuelve True para volver al menú principal
            else:
                print("Ingresa una opción válida.")
        except ValueError:
            print("Por favor, ingresa una opción válida.")