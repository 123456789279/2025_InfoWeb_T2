from datetime import datetime

class Agendamento:
   def __init__(self, id, data, confirmado, id_funcionario):
      self.set_id(id)
      self.set_data(data)
      self.set_confirmado(confirmado)
      self.set_id_funcionario(id_funcionario)
   def __str__(self):
     return f"{self.__id} - {self.__data.strftime('%d/%m/%Y %H:%M')} - {self.__confirmado}"
   def get_id(self): 
     return self.__id
   def get_data(self): 
     return self.__data
   def get_confirmado(self): 
     return self.__confirmado
   def get_id_funcionario(self): 
     return self.__id_funcionario
   def set_id(self, id): 
     self.__id = id
   def set_data(self, data): 
     if data == 0: raise ValueError("data inválida") 
     self.__data = data
   def set_confirmado(self, confirmado): 
     self.__confirmado = confirmado
   def set_id_funcionario(self, id_funcionario): 
     self.__id_funcionario = id_funcionario
   def to_json(self):
     dic = {"id":self.__id, "data":self.__data.strftime("%d/%m/%Y %H:%M"),
       "confirmado":self.__confirmado, "id_funcionario":self.__id_funcionario,}
     return dic
   @staticmethod
   def from_json(dic):
     agendamento = Agendamento(dic["id"], datetime.strptime(dic["data"], "%d/%m/%Y %H:%M"), dic["confirmado"], dic["id_funcionario"])
     agendamento.set_confirmado(dic["confirmado"])
     agendamento.set_id_funcionario(dic["id_funcionario"])
     return agendamento
   
import json
from models.dao import DAO

class AgendamentoDAO(DAO):
    @classmethod
    def abrir(cls):
        cls._objetos = []
        try:
            with open("agendamentos.json", mode ="r") as arquivo:
                list_dic = json.load(arquivo)
                for dic in list_dic:
                    obj = Agendamento.from_json(dic)
                    cls._objetos.append(obj)
        except FileNotFoundError:
            pass
    
    @classmethod
    def salvar(cls):
        with open("agendamentos.json", mode ="w") as arquivo:
            json.dump(cls._objetos, arquivo, default = Agendamento.to_json)