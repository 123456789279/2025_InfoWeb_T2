class conta_bancaria:
    def _init_(self):
        self.nome = "Gilbert"
        self.numero = 1028922
        self.saldo = 100.000
    def deposito(self):
        self.saldo += self.numero
        print(f"Depósito de {self.valor} realizado com sucesso. Novo saldo: {self.saldo}")
    def saque(self):
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