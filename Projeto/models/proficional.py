class Proficional:
    def __init__(self, id, nome, especialidade, conselho, email, senha):
        self.set_id(id)
        self.set_nome(nome)
        self.set_especialidade(especialidade)
        self.set_conselho(conselho)
        self.set_email(email)
        self.set_senha(senha)
    def __str__(self):
        return f"{self._id}-{self._nome}-{self._especialidade}-{self._conselho}"
    def get_id(self):
        return self._id
    def get_nome(self):
        return self._nome
    def get_especialidade(self):
        return self._especialidade 
    def get_conselho(self):
        return self._conselho
    def get_email(self):
        return self._email
    def get_senha(self):
        return self._senha
    def set_id(self, id):
        self._id = id
    def set_nome(self, nome):
        if nome == "": raise ValueError("Nome inválido")
        self._nome = nome
    def set_especialidade(self, especialidade):
        self._especialidade = especialidade
    def set_conselho(self, conselho):
        self._conselho = conselho
    def set_email(self, email):
        if email == "": raise ValueError("E-mail inválido")
        self._email= email
    def set_senha(self, senha):
        if senha == 0: raise ValueError("senha inválida")
        self._senha = senha
    def to_json(self):
        dic = {"id":self._id, "nome":self._nome, "especialidade":self._especialidade, "conselho":self._conselho, "email":self._email, "senha":self._senha}
        return dic
    @staticmethod
    def from_json(dic):
        return Proficional(dic["id"], dic["nome"], dic["especialidade"], dic["conselho"], dic["email"], dic["senha"])
    
import json
from models.dao import DAO

class ProficionalDAO(DAO):
    @classmethod
    def abrir(cls):
        cls._objetos = []
        try:
            with open("proficional.json", mode="r") as arquivo:
                list_dic = json.load(arquivo)
                for dic in list_dic:
                    obj = Proficional.from_json(dic)
                    cls._objetos.append(obj)
        except FileNotFoundError:
            pass
    
    @classmethod
    def salvar(cls):
        with open("proficional.json", mode="w") as arquivo:
            json.dump(cls._objetos, arquivo, default = Proficional.to_json)

    @classmethod
    def alterar_senha(cls, obj, id, senha):
        aux = cls.listar_id(obj.get_id())
        aux2 = cls.listar_senha(obj.get_senha())
        if aux != None and aux2 != None:
          cls._objetos.remove(aux)
          cls._objetos.remove(aux2)
          cls._objetos.append(obj)
          cls.salvar()

