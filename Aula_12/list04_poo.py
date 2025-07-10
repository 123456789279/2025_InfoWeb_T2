"""
# 1. Jogo de Bingo
#import random
#class Bingo:
#    def __init__(self, numBolas):
#        self.__numBolas = numBolas
#        self.__Bolas = []
#    def set__numBolas(self, numBolas):
#        if numBolas <= 5: raise ValueError("O numBolas deve ser no minimo 5")
#        self.__numBolas = numBolas
#    def set__Bolas(self, Bolas):
#        if Bolas <= 5: raise ValueError("O Bolas deve ser no minimo 5")
#        self.__Bolas = Bolas
#    def get__numBolas(self):
#        return self.__numBolas
#    def get__Bolas(self):
#        return self.__Bolas
#    def sortear(self):
#        if len(self.__Bolas) == self.__numBolas:
#            return -1
#        x = random.randint(1, self.__numBolas)
#        while x in self.__Bolas:
#            x = random.randint(1, self.__numBolas)
#        self.__Bolas.append(x)
#        return x
#    def sorteados(self):
#        if self.__Bolas <= 5:
#          return sorted(self.__Bolas)

#class BingoUI:
#    @staticmethod
#    def main():
#        op = 0
#        while op != 4:
#            op = BingoUI.menu()
#            if op == 1: self.__jogo = BingoUI.iniciar_jogo()
#            if op == 2: BingoUI.sortear(self.__jogo)
#            if op == 3: BingoUI.sorteados(self.__jogo)
#    @staticmethod
#    def set.__jogo(self, jogo)
#        self.__jogo = jogo
#    @staticmethod
#    def get.__jogo(self, jogo)
#        return self.__jogo
#    @staticmethod
#    def menu():
#        return int(input("1-Iniciar Jogo, 2-Sortear, 3-Sorteados, 4-Fim: "))
#    @staticmethod
#    def iniciar_self.__jogo():
#        self.__jogo = Bingo(int(input("Informe o número de bolas: ")))
#        return self.__jogo
#    @staticmethod
#    def sortear(self.__jogo):
        print(self.__jogo.sortear())
    @staticmethod
    def sorteados(self.__self.__jogo):
        print(self.__jogo.sorteados())

BingoUI.main()
"""

#2 Agenda de contatos
#class Contato:
#    def __init__(self, i, n, e, f):
#        self.__id = i
#        self.__nome = n
#        self.__email = e
#        self.__fone = f
#    def get_nome(self):
#        return self.__nome    
#    def __str__(self):
#        return f"{self.__id} - {self.__nome} - {self.__email} - {self.__fone}"

#class ContatoUI:
#    __contatos = []
#    @classmethod    
#    def main(cls):
#        op = 0
#        while op != 6:
#            op = ContatoUI.menu()
#            if op == 1: ContatoUI.inserir()
#            if op == 2: ContatoUI.listar()
#            if op == 3: ContatoUI.atualizar()
#            if op == 4: ContatoUI.excluir()
#            if op == 5: ContatoUI.pesquisar()
#    @classmethod    
#    def menu(cls):
#       print("1-Inserir, 2-Listar, 3-Atualizar, 4-Excluir, 5-Pesquisar, 6-Fim")
#       return int(input("Escolha uma opção: "))
#    @classmethod    
#    def inserir(cls):
#        id = int(input("Informe o id do contato: "))
#        nome = input("Informe o nome: ")
#        email = input("Informe o e-mail: ")
#        fone = input("Informe o fone: ")
#        c = Contato(id, nome, email, fone)
#        cls.__contatos.append(c)
#    @classmethod    
#    def listar(cls):
#        #print(cls.__contatos)
#        for c in cls.__contatos:
#            print(c)
#    @classmethod    
#    def atualizar(cls):
#        atualizar = input("Informe o id que deseja atualizar: ")
#        for c in cls.__contatos:
#            if c.get_atualizar().insert(2, atualizar): ContatoUI.insert(c)
#    @classmethod    
#    def excluir(cls):
#        excluir = input("Informe o id que deseja excluir: ")
#        for c in cls.__contatos:
#            if c.get_excluir().remove(excluir): ContatoUI.remove(c)
#    @classmethod    
#    def pesquisar(cls):
#        nome = input("Informe o nome: ")
#        for c in cls.__contatos:
#            if c.get_nome().startswith(nome): print(c)

#ContatoUI.main()

# 3. Cadastro de paises
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