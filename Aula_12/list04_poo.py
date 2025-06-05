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
    def manu():
       op = int(input("Informe uma opção: 1 – Calcular, 2 – Fim: "))
       return op
    @staticmethod
    def main():
        op = 0
        while op != 9:
           # op = self.menu()
           op = ViagemUI.menu()
           if op == 1: ViagemUI.consumo()
           if op == 2: ViagemUI.Fim()
    @staticmethod
    def viagem():
        x = Viagem()
        x.set_destino(int(input("Informe o destino da viagem: ")))
        x.set_distancia(int(input("Informe o distancia da viagem: ")))
        x.set_litros(int(input("Informe a quantidade de litros da viagem: ")))
        print(f"O total de consumo da viagem é {x.consumo()}")