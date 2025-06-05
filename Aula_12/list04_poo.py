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
        if distancia < 0: raise ValueError("A distancia percorrida deve ser maior que 0")
        self.__distancia = distancia
    def set__litros(self, litros):
        if litros < 0: raise ValueError("A quantidde de litros deve ser maior que 0")
        self.__litros = litros
    def get__destino(self):
        return self.__destino
    def get__distancia(self):
        return self.__distancia
    def get__litros(self):
        return self.__litros
    def consumo(self):
        return self.__distancia // self.__litros

class ViagemUI:
    @staticmethod
    def main():
      x = Viagem()