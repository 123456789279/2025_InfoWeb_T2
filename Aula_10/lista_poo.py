#1 - Circulo
#class circulo:
#    def _init_(self):
#        self.__raio = 10
#    def set_area(self):
#        A = 3,14 * self.__raio**2
#        return A
#    def get_circuferencia(self):
#        C = 2 * 3,14 * self.__raio
#        return C

#x = circulo()
#x.__raio = 5
#print(x.set__area()) # o self e x
#print(x.get__circuferencia()) # o self e x    

#2 - Uma Viagem
#class viagem:
#    def _init_(self):
#        self.__distancia = 200
#        self.__tempo = 2
#    def set__velocidade_media(self):
#        vm = self.__distancia / self.__tempo
#        return vm

#x = viagem()
#x.distancia = 200
#x.tempo = 4
#print(x.set__velocidade_media()) # o self e x

#3 - Uma Conta Banacaria
class conta_bancaria:
    def _init_(self):
        self.__titular = ""
        self.__numero = ""
        self.__saldo = 0.0
    def set_titular(self, t):
        if t == "": raise ValueError()
        self.__titular = t
    def get_titular(self):
        return self.__titular
    def get_saldo(self):
        return self.__saldo
    def set__deposito(self):
        self.__saldo += self.__numero
        print(f"Depósito de {self.__valor} realizado com sucesso. Novo saldo: {self.__saldo}")
    def get__saque(self):
        if 0 < self.__numero <= self.__saldo:
            self.__saldo -= self.__numero
            print(f"Saque de {self.__numero} realizado com sucesso. Novo saldo: {self.__saldo}")
        else:
            print("Saque não autorizado. Saldo insuficiente ou valor inválido.")

x = conta_bancaria()
x.titular = "Ranielly"
x.numero = 1.000
x.saldo = 100.000
print(x.deposito())
print(x.saque())

