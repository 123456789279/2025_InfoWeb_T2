class Empregador:
    def __init__(self, id, nome, email, senha):
        self.set_id(id)
        self.set_nome(nome)
        self.set_email(email)
        self.set_senha(senha)
    def __str__(self):
        return f"{self._id}-{self._nome}"
    def get_id(self):
        return self._id
    def get_nome(self):
        return self._nome
    def get_email(self):
        return self._email
    def get_senha(self):
        return self._senha
    def set_id(self, id):
        self._id = id
    def set_nome(self, nome):
        if nome == "": raise ValueError("Nome inválido")
        self._nome = nome
    def set_email(self, email):
        if email == "": raise ValueError("E-mail inválido")
        self._email= email
    def set_senha(self, senha):
        if senha == 0: raise ValueError("senha inválida")
        self._senha = senha
    def to_json(self):
        dic = {"id":self._id, "nome":self._nome, "email":self._email, "senha":self._senha}
        return dic
    @staticmethod
    def from_json(dic):
        return Empregador(dic["id"], dic["nome"], dic["email"], dic["senha"])
    
import json
from models.dao import DAO

class EmpregadorDAO(DAO):
    @classmethod
    def abrir(cls):
        cls._objetos = []
        try:
            with open("empregador.json", mode="r") as arquivo:
                list_dic = json.load(arquivo)
                for dic in list_dic:
                    obj = Empregador.from_json(dic)
                    cls._objetos.append(obj)
        except FileNotFoundError:
            pass
    
    @classmethod
    def salvar(cls):
        with open("empregador.json", mode="w") as arquivo:
            json.dump(cls._objetos, arquivo, default = Empregador.to_json)
