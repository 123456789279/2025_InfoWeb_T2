#1. Uma Viagem
class Viagem:
    def __init__(self):
        self.__destino = ""
        self.__distancia = ""
        self.__litros = ""
    def set__destino(self, destino):
        if destino < 0: raise ValueError("O destino deve ser maior que 0")
        self.__destino = destino
    def set__distancia(self, distancia):
        if distancia < 0: raise ValueError("A distancia deve ser maior que 0")
        self.__distancia = distancia
    def get__destino(self):
        return self.__destino
    def get__distancia(self):
        return self.__distancia