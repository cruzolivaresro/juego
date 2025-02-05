import objetos

def leer_archivo(archivo):
    with open(archivo, "r") as archivo:
        contenido = archivo.readlines()
        for linea in contenido:
            atributos = linea.split(",")
            if atributos[2] != 0:
                jugador = objetos.Guerrero(atributos[0], atributos[1], atributos[2], atributos[3])
            else:
                jugador = objetos.Mago(atributos[0], atributos[1], atributos[2], atributos[3])
    return jugador
