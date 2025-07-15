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
        if self.__distancia <= 3: raise ValueError("A Distancia Percorrida deve ter hora, minuto e segundo")
        self.__distancia = distancia
    def set__tempo(self, tempo):
        self.__tempo = datetime.timedelta(hours=int(input()), minutes=int(input()), seconds=int(input()))
        if self.__tempo <= 3: raise ValueError("O Tempo da Corrida deve ter hora, minuto e segundo")
        self.__tempo = tempo
    def set__Treino(self, Treino):
        self.__Treino = Treino                    
    def get__id(self):
        return self.__id
    def get__data(self):
        return self.__data
    def get__distancia(self):
        return self.__distancia
    def get__Treino(self):
        return self.__Treino
    def get__Treino(self):
        return self.__tempo    
    def Treino(self, id, data, distancia, tempo):
        self.__Treino = {id:self.__id,
                  data:self.__data,
                  distancia:self.__distancia,
                  tempo:self.__tempo}
    def __str__(self):
        return Treino
    
class TreinoUI:
    @staticmethod
    def main():
        op = 0
        while op != 4:
            op = TreinoUI.menu()
            if op == 1: TreinoUI.inserir()
            if op == 2: TreinoUI.listar()
            if op == 3: TreinoUI.atualizar()
            if op == 4: TreinoUI.excluir()
    @staticmethod        
    def menu():
       print("1-Inserir, 2-Listar, 3-Atualizar, 4-Excluir, 5-Fim")
       return int(input("Escolha uma opção: "))
    @staticmethod
    def inserir(cls):
        id = int(input("Informe o id do jogador: "))
        data = datetime.datetime.strptime("Informe a data do treino: " f"{int(input())}/{int(input())}/{int(input())}", "%d:%m:%y")
        distancia = datetime.datetime.strptime("Informe a distancia percorrida: " f"{int(input())}:{int(input())}:{int(input())}", "%H:%M:%S")
        tempo = datetime.timedelta(hours=int(input(Informe)), minutes=int(input()), seconds=int(input()))

TreinoUI.main()