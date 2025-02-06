import sys, funciones

def juego():
    while True: # Ciclo principal del juego
        try:
            print("***** Menú *****")
            print("[0] Comienza la aventura.")
            print("[1] Escoge a tu personaje.")
            print("[2] Observa a tu personaje.")
            print("[3] Volver al menú anterior.")
            opcion = int(input("Elige una opción: "))
            if opcion == 0:
                pass
            if opcion == 1:
                funciones.print_lista_personajes("archivos/personajes.txt")
                eleccion = int(input("Elige un personaje: "))
                if eleccion in [0,1,2,3,4,5,6,7,8,9]:
                    personaje = funciones.elegir_personaje("archivos/personajes.txt", eleccion)
                    print(f"Elegiste a {personaje.nombre}")
                else:
                    print("Ingresa una opción válida.")
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