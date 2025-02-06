from abc import ABC, abstractmethod

class Equipo():
    def __init__(self):
        self._miembros = []

    def agregar_miembro(self, personaje):
        self._miembros.append(personaje)
        print(f"{personaje.nombre} se ha unido al equipo")

    def visualizar_equipo(self):
        if not self._miembros:
            print("No hay personajes en el equipo")
            return
    
        print("Tu equipo:")
        for i, personaje in enumerate(self._miembros, 1):
            if personaje.clase == "Guerrero":
                print(f" {i}. {personaje.nombre}, Vida: {personaje.vida}, Fuerza: {personaje.fuerza}")
            else:
                print(f" {i}. {personaje.nombre}, Vida: {personaje.vida}, Inteligencia: {personaje.inteligencia}")
            

class Persona(ABC):
    def __init__(self, nombre, vida, fuerza, inteligencia):
        #Recuerda que los atributos no deben cambiarse fuera de la clase:
        self.nombre = nombre
        self._vida = vida
        self._fuerza = fuerza
        self._inteligencia = inteligencia
        self._clase = ''

        @abstractmethod
        def atacar(self, objetivo):
            pass

        @abstractmethod
        def recibir_daño(self, cantidad):
            pass
        
        @abstractmethod
        def usar_pocion_vida(self, cantidad):
            pass

        def morir(self):
            return self._vida <= 0

class Guerrero(Persona):
    def __init__(self, nombre, vida, fuerza, inteligencia, clase = "Guerrero"):
        super().__init__(nombre, vida, fuerza, inteligencia)

    def atacar(self, objetivo):
        objetivo.recibir_daño(self._fuerza)
        print(f"{self.nombre} atacó a {objetivo.nombre} haciendo {self.fuerza} puntos de daño.")

    def recibir_daño(self, cantidad):
        self._vida -= cantidad
        print(f"La vida ha disminuido en {cantidad} puntos.")
    
    def usar_pocion_vida(self, cantidad):
        self._vida += cantidad
        print(f"La vida ha aumentado en {cantidad} puntos.")

    def usar_pocion_fuerza(self, cantidad):
        self._fuerza += cantidad
        print(f"La fuerza ha aumentado en {cantidad} puntos.")


class Mago(Persona):
    def __init__(self, nombre, vida, fuerza, inteligencia, clase = "Mago"):
        super().__init__(nombre, vida, fuerza , inteligencia)

    def atacar(self, objetivo):
        objetivo.recibir_daño(self._inteligencia)
        print(f"{self.nombre} atacó a {objetivo.nombre} haciendo {self._inteligencia} puntos de daño")
    
    def recibir_daño(self, cantidad):
        self._vida -= cantidad
        print(f"La vida ha disminuido en {cantidad} puntos.")
    
    def usar_pocion_vida(self, cantidad):
        self._vida += cantidad
        print(f"La vida ha aumentado en {cantidad} puntos.")

    def usar_pocion_inteligencia(self, cantidad):
        self._inteligencia += cantidad
        print(f"La inteligencia ha aumentado en {cantidad} puntos.")
