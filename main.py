import sys
import juego

def main():
    key = True  # Variable key para controlar el estado
    while key:  # Ciclo principal del juego
        try:
            print("Sean bienvenidos al torneo")
            print("[1] Iniciar registro")
            print("[2] Salir del torneo")
            opcion = int(input("Elige una opción: "))
            if opcion == 1:
                key = juego.juego(key)  # Llamamos a juego.py y obtenemos el valor de key
            elif opcion == 2:
                print("Cerrando juego")
                sys.exit()  # Sale del juego
            else:
                print("Ingresa una opción correcta")
        except ValueError:
            print("Por favor, ingresa una opción válida.")

# Llamada inicial
main()