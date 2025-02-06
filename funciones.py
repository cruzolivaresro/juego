import objetos

def print_lista_personajes(archivo):
    with open(archivo, "r") as archivo:
        contenido = archivo.readlines()
        for i, linea in enumerate(contenido):
            atributos = linea.split(",")
            print(f"[{i}]. {atributos[0]}")

def elegir_personaje(archivo, eleccion):
    with open(archivo, "r") as archivo:
        contenido = archivo.readlines()
        for i, linea in enumerate(contenido):
            if i == eleccion:
                atributos = linea.split(",")
                if atributos[2] != 0:
                    personaje = objetos.Guerrero(atributos[0], atributos[1], atributos[2], atributos[3])
                    return personaje
                else:
                    personaje = objetos.Mago(atributos[0], atributos[1], atributos[2], atributos[3])
                    return personaje