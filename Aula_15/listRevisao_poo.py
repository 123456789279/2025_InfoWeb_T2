# 01 - Um Treino
import datetime
class Treino:
    def __init__(self):
        self.__id = ""
        self.__data = ""
        self.__distancia = ""
        self.__tempo = ""
    def set__id(self, id):
        if self.__id <= 5: raise ValueError("O id deve ter no minimo 5 digitos")
        self.__id = id
    def set__data(self, data):
        self.__data = datetime.datetime.strptime(f"{int(input())}/{int(input())}/{int(input())}", "%d:%m:%y")
        if self.__data <= 3: raise ValueError("A Data do Treino deve ter ano, mes e dia")
        self.__data = data
    def set__distancia(self, distancia):
        self.__distancia = datetime.datetime.strptime(f"{int(input())}:{int(input())}:{int(input())}", "%H:%M:%S")
        if self.__distancia <= 3: raise ValueError("A Distancia percorrida deve ter hora, minuto e segundo")
        self.__data = distancia                

    def get__id(self):
        return self.__id
    def get__data(self):
        return self.__data