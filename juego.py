import sys, funciones

def juego():
    while True:  
        try:
            print("***** Menú *****")
            print("[1] Escoge a tu equipo")
            print("[2] Observa a tu equipo")
            print("[3] Volver al menú anterior")
            opcion = int(input("Elige una opción: "))
            if opcion == 1:
                print("Elige a un personaje")
                personaje = funciones.leer_archivo("archivos/personajes.txt")
                print(f"Haz elegido a {personaje.nombre}")
                
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