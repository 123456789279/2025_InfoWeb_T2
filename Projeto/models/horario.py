from datetime import datetime
class Horario:
   def __init__(self, id, data):
      self.__id = id
      self.__data = data
      self.__confirmado = False
      self.__id_cliente = 0
      self.__id_servico = 0
      self.__id_proficional =- 0
   def __str__(self):
     return f"{self.__id} - {self.__data.strftime('%d/%m/%Y %H:%M')} - {self.__confirmado}"
   def get_id(self): 
     return self.__id
   def get_data(self): 
     return self.__data
   def get_confirmado(self): 
     return self.__confirmado
   def get_id_cliente(self): 
     return self.__id_cliente
   def get_id_servico(self): 
     return self.__id_servico
   def get_id_proficional(self): 
     return self.__id_proficional
   def set_id(self, id): 
     self.__id = id
   def set_data(self, data): 
     if data < 0: raise ValueError("data inválida") 
     self.__data = data
   def set_confirmado(self, confirmado): 
     self.__confirmado = confirmado
   def set_id_cliente(self, id_cliente): 
     self.__id_cliente = id_cliente
   def set_id_servico(self, id_servico): 
     self.__id_servico = id_servico
   def set_id_proficional(self, id_proficional): 
     self.__id_proficional = id_proficional
   def to_json(self):
     dic = {"id":self.__id, "data":self.__data.strftime("%d/%m/%Y %H:%M"),
       "confirmado":self.__confirmado, "id_cliente":self.__id_cliente,
       "id_servico":self.__id_servico, "id_proficional":self.__id_proficional}
     return dic
   @staticmethod
   def from_json(dic):
     horario = Horario(dic["id"], datetime.strptime(dic["data"], "%d/%m/%Y %H:%M"))
     horario.set_confirmado(dic["confirmado"])
     horario.set_id_cliente(dic["id_cliente"])
     horario.set_id_servico(dic["id_servico"])
     horario.set_id_proficional(dic["id_proficional"])
     return horario
   
import json
from models.dao import DAO

class HorarioDAO(DAO):
    @classmethod
    def salvar(cls):
        with open("horarios.json", mode ="w") as arquivo:
            json.dump(cls.__objetos, arquivo, default = Horario.to_json)

    @classmethod
    def abrir(cls):
      cls.__objetos = []
      try:
        with open("horarios.json", mode ="r") as arquivo:
          list_dic = json.load(arquivo)
          for dic in list_dic:
            obj = Horario.from_json(dic)
            cls.__objetos.append(obj)
      except FileNotFoundError:
        pass