#1 - Circulo
class circulo:
    def _init_(self):
        self.__raio = 10
    def set_area(self):
        A = 3,14 * self.__raio**2
        return A
    def get_circuferencia(self):
        C = 2 * 3,14 * self.__raio
        return C
    
x = circulo()
x.__raio = 5
print(x.set__area()) # o self e x
print(x.get__circuferencia()) # o self e x    

#2 - Uma Viagem
class viagem:
    def _init_(self):
        self.__distancia = 200
        self.__tempo = 2
    def set__velocidade_media(self):
        vm = self.__distancia / self.__tempo
        return vm

x = viagem()
x.distancia = 200
x.tempo = 4
print(x.set__velocidade_media()) # o self e x

#3 - Uma Conta Banacaria
class conta_bancaria:
    def _init_(self):
        self.__nome = "Gilbert"
        self.__numero = 1028922
        self.__saldo = 100.000
    def set__deposito(self):
        self.__saldo += self.numero
        print(f"Depósito de {self.valor} realizado com sucesso. Novo saldo: {self.saldo}")
    def get__saque(self):
        if 0 < self.numero <= self.saldo:
            self.saldo -= self.numero
            print(f"Saque de {self.numero} realizado com sucesso. Novo saldo: {self.saldo}")
        else:
            print("Saque não autorizado. Saldo insuficiente ou valor inválido.")

x = conta_bancaria()
x.nome = "Ranielly"
x.numero = 1.000
x.saldo = 100.000
print(x.deposito())
print(x.saque())

