# 1. Um Paciente
import datetime
class Paciente:
    def __init__(self):
        self.__nome = ""
        self.__cpf = ""
        self.__telefone = ""
        self.__nascimento = ""
    def set__nome(self, nome):
        nome = len(self.__nome)
        if self.__nome <= 5: raise ValueError("O nome deve ter no minimo 5 letras")
        self.__nome = nome
    def set__cpf(self, cpf):
        if self.__cpf <= 5: raise ValueError("O cpf deve ter no minimo 5 digitos")
        self.__cpf = cpf
    def set__telefone(self, telefone):
        if self.__telefone <= 5: raise ValueError("O telefone deve ter no minimo 5 digitos")
        self.__telefone = telefone
    def set__nascimento(self, nascimento):
        nascimento = datetime.datetime(int(input()), int(input()), int(input()))
        self.__nascimento = nascimento
    def get__nome(self):
        return self.__nome
    def get__cpf(self):
        return self.__cpf
    def get__telefone(self):
        return self.__telefone
    def get__nascimento(self):
        return self.__nascimento
    def idade(self, nascimento):
        nascimento = datetime.datetime.strptime("%m/%Y ")
        return nascimento.month and nascimento.year
    def ToString(self):
        print(f"Nome de um paciente: {self.__nome}")
        print(f"cpf de um paciente: {self.__cpf}")
        print(f"Telefone de um paciente: {self.__telefone}")
        print(f"Data de Nascimento de um paciente: {self.__nascimento}")

class PacienteUI:
    @classmethod
    def main():
        op = 0
        while op != 2:
            op = PacienteUI.menu()
            if op == 1: PacienteUI.inserir()
            if op == 2: PacienteUI.listar()
    @classmethod    
    def menu(cls):
        print("1-Inserir,2-Listar, 3-Fim")
        return int(input("Escolha uma opção: "))
    @classmethod    
    def inserir(cls):
        nome = input("Informe o nome do paciente: ")
        cpf = int(input("Informe o cpf do paciente: "))
        telefone = int(input("Informe o telefone do paciente: "))
        nascimento = datetime.datetime(int(input("Informe o dia de nascimento do paciente: ")), int(input("Informe o mes de nascimento do paciente: ")), int(input("Informe o ano de nascimento do paciente: ")))
        paciente = Paciente(nome, cpf, telefone, nascimento)
        cls.__paciente.append(paciente)
    @classmethod    
    def listar(cls):
        for c in cls.__contatos:
            print(c)

PacienteUI.main()
    