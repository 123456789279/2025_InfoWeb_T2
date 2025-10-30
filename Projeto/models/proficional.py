class Proficional:
    def __init__(self, id, nome, especialidade, conselho, email, senha):
        self.__id = 0
        self.__nome = ""
        self.__especialidade = ""
        self.__conselho = ""
        self.__email = ""
        self.__senha = 0
    def __str__(self):
        return f"{self.__id}-{self.__nome}-{self.__especialidade}-{self.__conselho}"
    def get_id(self):
        return self.__id
    def get_nome(self):
        return self.__nome
    def get_especialidade(self):
        return self.__especialidade 
    def get_conselho(self):
        return self.__conselho
    def get_email(self):
        return self.__email
    def get_senha(self):
        return self.__senha
    def set_id(self, id):
        self.__id = id
    def set_nome(self, nome):
        if nome == "": raise ValueError("Nome inválido")
        self.__nome = nome
    def set_especialidade(self, especialidade):
        self.__especialidade = especialidade
    def set_conselho(self, conselho):
        self.__conselho = conselho
    def set_email(self, email):
        if email == "": raise ValueError("E-mail inválido")
        self.__email= email
    def set_senha(self, senha):
        if senha < 0: raise ValueError("senha inválida")
        self.__senha = senha
    def to_json(self):
        dic = {"id":self.__id, "nome":self.__nome,"especialidade":self.__especialidade, "conselho":self.__conselho, "email":self.__email, "senha":self.__senha}
        return dic
    @staticmethod
    def from_json(dic):
        return Proficional(dic["id"], dic["nome"], dic["especialidade"], dic["conselho"], dic["email"], dic["senha"])
    
import json
from models.dao import DAO

class ProficionalDAO(DAO):
    @classmethod
    def alterar_senha(cls, obj):
      aux = cls.listar_id(obj.get_id())
      if aux != None:
        cls.__objetos.remove(aux)
        cls.__objetos.append(obj)
        cls.salvar()

    @classmethod
    def salvar(cls):
      with open("proficional.json", mode="w") as arquivo:
        json.dump(cls.__objetos, arquivo, default = Proficional.to_json)

    @classmethod
    def abrir(cls):
      cls.__objetos = []
      try:
         with open("proficional.json", mode="r") as arquivo:
           list_dic = json.load(arquivo)
           for dic in list_dic:
             obj = Proficional.from_json(dic)
             cls.__objetos.append(obj)
      except FileNotFoundError:
         pass
