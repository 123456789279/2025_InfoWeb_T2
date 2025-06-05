# 1. Uma Viagem
#class Viagem:
#    def __init__(self):
#        self.__destino = ""
#        self.__distancia = ""
#        self.__litros = ""
#    def set__destino(self, destino):
#        if destino < 0: raise ValueError("O destino deve ser maior que 0")
#        self.__destino = destino
#    def set__distancia(self, distancia):
#        if distancia < 0: raise ValueError("A distancia percorrida deve ser maior que 0")
#        self.__distancia = distancia
#    def set__litros(self, litros):
#        if litros < 0: raise ValueError("A quantidde de litros deve ser maior que 0")
#        self.__litros = litros
#    def get__destino(self):
#        return self.__destino
#    def get__distancia(self):
#        return self.__distancia
#    def get__litros(self):
#        return self.__litros
#    def consumo(self):
#        return self.__distancia // self.__litros

#class ViagemUI:
#    @staticmethod
#    def menu():
#       op = int(input("Informe uma opção: 1 – Calcular, 2 – Fim: "))
#       return op
#    @staticmethod
#    def main():
#        op = 0
#        while op != 9:
#           op = self.menu()
#           op = ViagemUI.menu()
#           if op == 1: ViagemUI.consumo()
#           if op == 2: ViagemUI.fim()
#    @staticmethod
#    def consumo():
#        x = Viagem()
#        x.set_destino(int(input("Informe o destino da viagem: ")))
#        x.set_distancia(int(input("Informe o distancia da viagem: ")))
#        x.set_litros(int(input("Informe a quantidade de litros da viagem: ")))
#        print(f"O total de consumo da viagem é {x.consumo()}")
#    @staticmethod
#    def fim():
#        print("Programa encerrado")

#ViagemUI.main()

# 2. Densidade de paises
#class Pais:
#    def __init__(self):
#        self.__nome = ""
#        self.__populacao = ""
#        self.__area = ""
#    def set__nome(self, nome):
#        if len(nome) < 0: raise ValueError("O nome deve ter mais que 0 letras")
#        self.__nome = nome
#    def set__populacao(self, populacao):
#        if populacao < 0: raise ValueError("A populacao deve ser maior que 0")
#        self.__populacao = populacao
#    def set__area(self, area):
#        if area < 0: raise ValueError("A area deve ser maior que 0 ")
#        self.__area = area
#    def get__nome(self):
#        return self.__nome
#    def get__populacao(self):
#        return self.__populacao
#    def get__area(self):
#        return self.__area
#    def densidade(self):
#        return self.__populacao // self.__area
    
#class PaisUI:
#    @staticmethod
#    def menu():
#       op = int(input("Informe uma opção: 1 – Calcular, 2 – Fim: "))
#       return op
#    @staticmethod
#    def main():
#        op = 0
#        while op != 9:
#           op = PaisUI.menu()
#           if op == 1: PaisUI.densidade()
#           if op == 2: PaisUI.fim()
#    @staticmethod
#    def densidade():
#        x = Pais()
#        x.set_nome(int(input("Informe o nome do pais: ")))
#        x.set_populacao(int(input("Informe o popilacao do pais: ")))
#        x.set_area(int(input("Informe a area do pais: ")))
#        print(f"O total de consumo da viagem é {x.densidade()}")
#    @staticmethod
#    def fim():
#        print("Programa encerrado")

#PaisUI.main()