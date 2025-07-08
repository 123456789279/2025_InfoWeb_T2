# 1. Um Paciente
import datetime
class Paciente:
    def __init__(self):
        self.__nome = ""
        self.__cpf = ""
        self.__telefone = ""
        self.__nascimento = ""
    def set__nome(self, nome):
        self.__nome = nome
    def set__cpf(self, cpf):
        self.__cpf = cpf
    def set__telefone(self, telefone):
        self.__telefone = telefone
    def set__nascimento(self, nascimento):
        self.__nascimento = nascimento