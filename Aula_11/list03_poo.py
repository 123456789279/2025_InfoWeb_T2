class Retangulo:
    def __init__(self):
        self.__base = ""
        self.__altura = ""
    def set__base(self, base):
        if base > 0: raise ValueError("A base deve ser maior que 0")
        self.__base = base
    def set__altura(self, altura):
        if altura > 0: raise ValueError("A altura deve ser maior que 0")
        self.__altura = altura
    def get__base(self):
        return self.__base
    def get__altura(self):
        return self.__altura
    def calcular_area(self):
        if set.__base % 2 == 0 and set.__altura % 2 == 0: raise ValueError("A base e a altura devem ser maiores que 0")
        set.__base * set.__altura
    def calcular_diagonal(self):
        if set.__base % 2 == 0 and set.__altura % 2 == 0: raise ValueError("A base e a altura devem ser maiores que 0")
        import math
        math.sqrt(set.__base ^ 2 + set.__altura ^ 2)
