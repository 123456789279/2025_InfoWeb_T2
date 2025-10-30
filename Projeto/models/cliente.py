import json

class Cliente:
    def __init__(self, id, nome, email, fone, senha):
        self.__id = 0
        self.__nome = ""
        self.__email = ""
        self.__fone = 0
        self.__senha = 0
    def get_id(self): 
        return self.__id
    def get_nome(self):
        return self.__nome
    def get_email(self): 
        return self.__email
    def get_fone(self): 
        return self.__fone
    def get_senha(self): 
        return self.__senha
    def set_id(self, id): 
        self.__id = id
    def set_nome(self, nome):
        if nome == "": raise ValueError("Nome inválido")
        self.__nome = nome
    def set_email(self, email):
        if email == "": raise ValueError("E-mail inválido") 
        self.__email = email
    def set_fone(self, fone): 
        self.__fone = fone
    def set_senha(self, senha):
        if senha < 0: raise ValueError("senha inválida") 
        self.__senha = senha
    def to_json(self):
        dic = {"id":self.__id, "nome":self.__nome, "email":self.__email, "fone":self.__fone, "senha":self.__senha}
        return dic  
    @staticmethod
    def from_json(dic):
        return Cliente(dic["id"], dic["nome"], dic["email"], dic["fone"], dic["senha"])
    def __str__(self):
        return f"{self.__id} - {self.__nome} - {self.__email} - {self.__fone} - {self.__senha}"

import json
from models.dao import DAO

class ClienteDAO(DAO):
    @classmethod
    def abrir(cls):
        cls.__objetos = []
        try:
            with open("clientes.json", mode="r") as arquivo:
                list_dic = json.load(arquivo)
                for dic in list_dic:
                    obj = Cliente.from_json(dic)
                    cls.__objetos.append(obj)
        except FileNotFoundError:
            pass 

    @classmethod
    def salvar(cls):
        with open("clientes.json", mode="w") as arquivo:
            json.dump(cls.__objetos, arquivo, default = Cliente.to_json)       